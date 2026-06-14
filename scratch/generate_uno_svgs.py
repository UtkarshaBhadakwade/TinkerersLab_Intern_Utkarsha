import os

image_dir = r"c:\Users\hp\OneDrive\Desktop\TinkeresLab\image"
os.makedirs(image_dir, exist_ok=True)

defs = """<defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255, 255, 255, 0.03)" stroke-width="1"/>
    </pattern>
    <linearGradient id="boardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#006468"/>
        <stop offset="100%" stop-color="#004d50"/>
    </linearGradient>
    <linearGradient id="chipGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#2a2a2a"/>
        <stop offset="100%" stop-color="#111111"/>
    </linearGradient>
</defs>"""

def draw_uno(x, y, scale=1.0, highlight="none"):
    # highlight can be: "none", "power", "digital", "analog", "comm", "all"
    w = 270 * scale
    h = 200 * scale
    
    # Highlight logic
    c_pwr = "#ffd700" if highlight in ["power", "all"] else "#555"
    c_dig = "#ffd700" if highlight in ["digital", "all"] else "#555"
    c_ana = "#ffd700" if highlight in ["analog", "all"] else "#555"
    c_com = "#ffd700" if highlight in ["comm", "all"] else "#555"
    
    # Overrides for communication overlapping with digital/analog
    if highlight == "comm":
        c_dig = "#555"
        c_ana = "#555"
        c_com = "#ffd700"
    
    board = f"""
    <g transform="translate({x}, {y}) scale({scale})">
        <!-- Board base -->
        <path d="M -135 -100 L 135 -100 C 145 -100, 155 -90, 155 -80 L 155 80 C 155 90, 145 100, 135 100 L -135 100 C -145 100, -155 90, -155 80 L -155 -80 C -155 -90, -145 -100, -135 -100 Z" fill="url(#boardGrad)" stroke="#00979d" stroke-width="2"/>
        
        <!-- USB Port (Type B) -->
        <rect x="-165" y="-85" width="40" height="45" rx="3" fill="#c0c0c0" stroke="#888" stroke-width="2"/>
        <rect x="-155" y="-75" width="20" height="25" fill="#e6e6e6" rx="2"/>
        
        <!-- Power Jack -->
        <rect x="-170" y="45" width="45" height="35" rx="2" fill="#222" stroke="#111" stroke-width="1"/>
        <circle cx="-145" cy="62.5" r="8" fill="#111"/>
        
        <!-- ATmega328P Chip (DIP) -->
        <rect x="20" y="30" width="100" height="30" rx="3" fill="url(#chipGrad)" stroke="#444" stroke-width="1"/>
        <text x="70" y="48" fill="#fff" font-family="monospace" font-size="8" text-anchor="middle" opacity="0.6">ATMEGA328P-PU</text>
        <!-- DIP pins -->
    """
    for i in range(14):
        px = 24 + i * 7
        board += f'<rect x="{px}" y="25" width="3" height="5" fill="#bbb"/>'
        board += f'<rect x="{px}" y="60" width="3" height="5" fill="#bbb"/>'

    board += """
        <!-- ATmega16U2 (USB Chip) -->
        <rect x="-80" y="-40" width="20" height="20" rx="2" fill="url(#chipGrad)" stroke="#444" stroke-width="1"/>
        
        <!-- Reset Button -->
        <rect x="30" y="-95" width="20" height="15" rx="2" fill="#dcdcdc" stroke="#999" stroke-width="1"/>
        <circle cx="40" cy="-87.5" r="4" fill="#e74c3c"/>

        <!-- Top Header Pins (Digital 0-13, AREF, GND, SDA, SCL) -->
        <rect x="-10" y="-95" width="150" height="12" fill="#222" rx="2"/>
        <!-- Bottom Header Pins (Power & Analog) -->
        <rect x="-60" y="83" width="70" height="12" fill="#222" rx="2"/>
        <rect x="25" y="83" width="60" height="12" fill="#222" rx="2"/>
        
        <!-- ICSP Header -->
        <rect x="130" y="10" width="20" height="30" fill="#222" rx="2"/>
    """
    
    # Top Header (Digital / Comm)
    for i in range(14):
        px = -5 + i * 10
        # D0, D1 (UART) -> Comm, D2-D13 -> Digital, 10,11,12,13 (SPI) -> Comm
        col = c_dig
        if i in [0, 1, 10, 11, 12, 13] and highlight == "comm": col = c_com
        board += f'<circle cx="{px}" cy="-89" r="2.5" fill="{col}"/>'
    
    # Top Header remaining (GND, AREF, SDA, SCL)
    for i in range(4):
        px = 135 + i * 10
        col = c_pwr if i < 2 else (c_com if highlight == "comm" else c_ana) # roughly SDA/SCL are I2C
        board += f'<circle cx="{px}" cy="-89" r="2.5" fill="{col}"/>'

    # Bottom Header Power (VIN, GND, GND, 5V, 3V3, RESET, IOREF)
    for i in range(7):
        px = -55 + i * 9.5
        col = c_pwr
        board += f'<circle cx="{px}" cy="89" r="2.5" fill="{col}"/>'

    # Bottom Header Analog (A0 - A5)
    for i in range(6):
        px = 30 + i * 9.5
        col = c_ana
        if i in [4, 5] and highlight == "comm": col = c_com # A4/A5 are SDA/SCL too
        board += f'<circle cx="{px}" cy="89" r="2.5" fill="{col}"/>'

    # ICSP Header (SPI)
    for i in range(2):
        for j in range(3):
            px = 135 + i * 10
            py = 15 + j * 10
            col = c_com if highlight == "comm" else ("#ffd700" if highlight == "all" else "#555")
            board += f'<circle cx="{px}" cy="{py}" r="2.5" fill="{col}"/>'

    board += "</g>"
    return board

# SVG Generators

def make_svg(title, desc, highlight, extra_content=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{desc}</desc>
  <rect width="1200" height="650" fill="#071014" rx="12"/>
  {defs}
  <rect width="1200" height="650" fill="url(#grid)" rx="12"/>
  <text x="600" y="80" text-anchor="middle" fill="#00ffd5" font-size="36" font-family="Arial" font-weight="bold">{title}</text>
  {draw_uno(600, 360, 1.4, highlight)}
  {extra_content}
</svg>"""

# 1. Overview
extra_1 = """
  <g font-family="Arial" font-size="16" fill="#f6fbff">
    <path d="M 330 240 L 250 240 L 200 220" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="240" y="255" text-anchor="middle" fill="#20d6b5">USB Type-B Port</text>
    <path d="M 330 420 L 250 420 L 200 440" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="240" y="410" text-anchor="middle" fill="#20d6b5">Power Jack</text>
    <path d="M 720 400 L 800 400 L 850 380" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="810" y="415" text-anchor="middle" fill="#20d6b5">ATmega328P Chip</text>
    <path d="M 720 220 L 800 220 L 850 200" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="810" y="235" text-anchor="middle" fill="#20d6b5">Digital Header</text>
    <path d="M 640 480 L 700 520 L 750 520" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="760" y="525" text-anchor="start" fill="#20d6b5">Analog Header</text>
  </g>
"""
board_svg = make_svg("Arduino Uno Overview", "Arduino Uno full board reference", "all", extra_1)

# 2. Power Pins
extra_2 = """
  <g font-family="Arial" font-size="16" fill="#f6fbff">
    <rect x="480" y="500" width="220" height="30" rx="4" fill="#e74c3c"/>
    <path d="M 520 480 L 520 500" fill="none" stroke="#e74c3c" stroke-width="2"/>
    <text x="590" y="520" text-anchor="middle">Power Pins (VIN, 5V, 3.3V, GND)</text>
  </g>
"""
power_svg = make_svg("Arduino Uno Power Pins", "Power pins reference", "power", extra_2)

# 3. Digital Pins
extra_3 = """
  <g font-family="Arial" font-size="16" fill="#f6fbff">
    <rect x="500" y="180" width="200" height="30" rx="4" fill="#3498db"/>
    <path d="M 600 230 L 600 210" fill="none" stroke="#3498db" stroke-width="2"/>
    <text x="600" y="200" text-anchor="middle">Digital I/O Pins (D0 - D13)</text>
  </g>
"""
digital_svg = make_svg("Arduino Uno Digital Pins", "Digital pins reference", "digital", extra_3)

# 4. Analog Pins
extra_4 = """
  <g font-family="Arial" font-size="16" fill="#f6fbff">
    <rect x="620" y="500" width="180" height="30" rx="4" fill="#2ecc71"/>
    <path d="M 680 480 L 680 500" fill="none" stroke="#2ecc71" stroke-width="2"/>
    <text x="710" y="520" text-anchor="middle">Analog Pins (A0 - A5)</text>
  </g>
"""
analog_svg = make_svg("Arduino Uno Analog Pins", "Analog pins reference", "analog", extra_4)

# 5. Communication Pins
extra_5 = """
  <g font-family="Arial" font-size="14" fill="#f6fbff">
    <rect x="750" y="160" width="100" height="24" rx="4" fill="#f1c40f"/>
    <path d="M 780 230 L 800 184" fill="none" stroke="#f1c40f" stroke-width="2"/>
    <text x="800" y="177" text-anchor="middle" fill="#000" font-weight="bold">I2C (SDA/SCL)</text>

    <rect x="550" y="160" width="100" height="24" rx="4" fill="#3498db"/>
    <path d="M 650 230 L 600 184" fill="none" stroke="#3498db" stroke-width="2"/>
    <text x="600" y="177" text-anchor="middle" font-weight="bold">SPI (10-13)</text>
    
    <rect x="800" y="300" width="80" height="24" rx="4" fill="#3498db"/>
    <path d="M 790 370 L 840 324" fill="none" stroke="#3498db" stroke-width="2"/>
    <text x="840" y="317" text-anchor="middle" font-weight="bold">ICSP (SPI)</text>

    <rect x="400" y="160" width="100" height="24" rx="4" fill="#e67e22"/>
    <path d="M 500 230 L 450 184" fill="none" stroke="#e67e22" stroke-width="2"/>
    <text x="450" y="177" text-anchor="middle" font-weight="bold">UART (RX/TX)</text>
  </g>
"""
comm_svg = make_svg("Arduino Uno Communication Pins", "Communication pins reference", "comm", extra_5)

# 6. Complete Pinout
extra_6 = """
  <!-- Comprehensive Legends for Pinout -->
  <g font-family="Arial" font-size="14" font-weight="bold">
    <rect x="50" y="110" width="120" height="25" rx="4" fill="#e74c3c"/><text x="110" y="128" text-anchor="middle" fill="#fff">Power / GND</text>
    <rect x="180" y="110" width="120" height="25" rx="4" fill="#2ecc71"/><text x="240" y="128" text-anchor="middle" fill="#fff">Analog Pins</text>
    <rect x="310" y="110" width="120" height="25" rx="4" fill="#3498db"/><text x="370" y="128" text-anchor="middle" fill="#fff">Digital I/O</text>
    <rect x="440" y="110" width="120" height="25" rx="4" fill="#9b59b6"/><text x="500" y="128" text-anchor="middle" fill="#fff">PWM (~)</text>
    <rect x="570" y="110" width="120" height="25" rx="4" fill="#e67e22"/><text x="630" y="128" text-anchor="middle" fill="#fff">Hardware Serial</text>
  </g>
  <g font-family="Arial" font-size="14" fill="#f6fbff" font-weight="bold">
    <!-- Some representative side labels to make it look like a complete pinout -->
    <!-- D13 - D0 -->
    <path d="M 520 230 L 520 200 L 720 200 L 720 230" fill="none" stroke="#3498db" stroke-width="2"/>
    <text x="620" y="190" text-anchor="middle" fill="#3498db">D13 to D0 (Digital &amp; PWM)</text>

    <!-- A0 - A5 -->
    <path d="M 640 480 L 640 510 L 710 510 L 710 480" fill="none" stroke="#2ecc71" stroke-width="2"/>
    <text x="675" y="530" text-anchor="middle" fill="#2ecc71">A0 to A5</text>

    <!-- Power -->
    <path d="M 520 480 L 520 510 L 600 510 L 600 480" fill="none" stroke="#e74c3c" stroke-width="2"/>
    <text x="560" y="530" text-anchor="middle" fill="#e74c3c">Power Pins</text>
  </g>
"""
complete_svg = make_svg("Arduino Uno Complete Pinout", "Complete Uno pinout diagram", "all", extra_6)

with open(os.path.join(image_dir, "arduino_uno_board.svg"), "w", encoding="utf-8") as f:
    f.write(board_svg)
with open(os.path.join(image_dir, "arduino_uno_power_pins.svg"), "w", encoding="utf-8") as f:
    f.write(power_svg)
with open(os.path.join(image_dir, "arduino_uno_digital_pins.svg"), "w", encoding="utf-8") as f:
    f.write(digital_svg)
with open(os.path.join(image_dir, "arduino_uno_analog_pins.svg"), "w", encoding="utf-8") as f:
    f.write(analog_svg)
with open(os.path.join(image_dir, "arduino_uno_comm_pins.svg"), "w", encoding="utf-8") as f:
    f.write(comm_svg)
with open(os.path.join(image_dir, "arduino_uno_complete_pinout.svg"), "w", encoding="utf-8") as f:
    f.write(complete_svg)

print("Uno SVGs generated successfully!")
