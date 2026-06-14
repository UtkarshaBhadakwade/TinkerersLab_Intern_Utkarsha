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

def draw_mega(x, y, scale=1.0):
    # Mega width ~ 101.52 mm, height ~ 53.3 mm
    # Scaled up: 400px wide, 210px high
    w = 400 * scale
    h = 210 * scale
    
    board = f"""
    <g transform="translate({x}, {y}) scale({scale})">
        <!-- Board base -->
        <path d="M -180 -100 L 180 -100 C 190 -100, 200 -90, 200 -80 L 200 80 C 200 90, 190 100, 180 100 L -180 100 C -190 100, -200 90, -200 80 L -200 -80 C -200 -90, -190 -100, -180 -100 Z" fill="url(#boardGrad)" stroke="#00979d" stroke-width="2"/>
        
        <!-- USB Port (Type B) -->
        <rect x="-210" y="-85" width="40" height="45" rx="3" fill="#c0c0c0" stroke="#888" stroke-width="2"/>
        <rect x="-200" y="-75" width="20" height="25" fill="#e6e6e6" rx="2"/>
        
        <!-- Power Jack -->
        <rect x="-215" y="45" width="45" height="35" rx="2" fill="#222" stroke="#111" stroke-width="1"/>
        <circle cx="-190" cy="62.5" r="8" fill="#111"/>
        
        <!-- ATmega2560 Chip -->
        <!-- Square flat package (TQFP 100) -->
        <rect x="-20" y="-30" width="60" height="60" rx="3" fill="url(#chipGrad)" stroke="#444" stroke-width="1"/>
        <!-- Chip pins (simulated lines) -->
        <rect x="-25" y="-20" width="5" height="40" fill="#bbb"/>
        <rect x="40" y="-20" width="5" height="40" fill="#bbb"/>
        <rect x="-10" y="-35" width="40" height="5" fill="#bbb"/>
        <rect x="-10" y="30" width="40" height="5" fill="#bbb"/>
        <text x="10" y="0" fill="#fff" font-family="monospace" font-size="6" text-anchor="middle" opacity="0.6">ATMEGA</text>
        <text x="10" y="10" fill="#fff" font-family="monospace" font-size="6" text-anchor="middle" opacity="0.6">2560</text>
        
        <!-- ATmega16U2 (USB Chip) -->
        <rect x="-130" y="-40" width="25" height="25" rx="2" fill="url(#chipGrad)" stroke="#444" stroke-width="1"/>
        
        <!-- Reset Button -->
        <rect x="80" y="-95" width="20" height="15" rx="2" fill="#dcdcdc" stroke="#999" stroke-width="1"/>
        <circle cx="90" cy="-87.5" r="4" fill="#e74c3c"/>

        <!-- Top Header Pins (Digital 0-13, AREF, GND, SDA, SCL) -->
        <!-- Usually a long block from center to right edge -->
        <rect x="-60" y="-95" width="240" height="12" fill="#222" rx="2"/>
        <!-- Bottom Header Pins (Power & Analog 0-15) -->
        <!-- Power & A0-A7 -->
        <rect x="-110" y="83" width="180" height="12" fill="#222" rx="2"/>
        
        <!-- Double row header on the far right (Digital 22-53) -->
        <rect x="175" y="-80" width="18" height="160" fill="#222" rx="2"/>
        
        <!-- ICSP Header -->
        <rect x="-80" y="10" width="20" height="30" fill="#222" rx="2"/>
    """
    
    # Generate some gold pin dots for headers
    # Top header
    for i in range(24):
        px = -55 + i * 9.5
        board += f'<circle cx="{px}" cy="-89" r="2.5" fill="#ffd700"/>'
    # Bottom header
    for i in range(18):
        px = -105 + i * 9.5
        board += f'<circle cx="{px}" cy="89" r="2.5" fill="#ffd700"/>'
    # Right double header (16 pairs)
    for i in range(16):
        py = -75 + i * 10
        board += f'<circle cx="179" cy="{py}" r="2.5" fill="#ffd700"/>'
        board += f'<circle cx="189" cy="{py}" r="2.5" fill="#ffd700"/>'
        
    board += "</g>"
    return board

# 1. arduino_mega_board.svg
board_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
  <title id="title">Arduino Mega Board</title>
  <desc id="desc">Vector illustration of Arduino Mega 2560 microcontroller board.</desc>
  <rect width="1200" height="650" fill="#071014" rx="12"/>
  {defs}
  <rect width="1200" height="650" fill="url(#grid)" rx="12"/>
  
  <text x="600" y="80" text-anchor="middle" fill="#00ffd5" font-size="36" font-family="Arial" font-weight="bold">Arduino Mega 2560 Overview</text>
  <text x="600" y="120" text-anchor="middle" fill="rgba(246, 251, 255, 0.72)" font-size="18" font-family="Arial">A powerful board designed for complex projects requiring many I/O lines and memory.</text>
  
  <!-- Draw Mega -->
  {draw_mega(600, 360, 1.2)}

  <!-- Callouts -->
  <g font-family="Arial" font-size="16" fill="#f6fbff">
    <path d="M 330 260 L 250 260 L 200 240" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="240" y="275" text-anchor="middle" fill="#20d6b5">USB Type-B Port</text>
    
    <path d="M 330 420 L 250 420 L 200 440" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="240" y="410" text-anchor="middle" fill="#20d6b5">Power Jack</text>
    <text x="240" y="440" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="14">(7V - 12V input)</text>

    <path d="M 600 360 L 600 220 L 650 180" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="660" y="175" text-anchor="start" fill="#20d6b5">ATmega2560</text>
    <text x="660" y="195" text-anchor="start" fill="rgba(255,255,255,0.5)" font-size="14">256 KB Flash / 8 KB SRAM</text>

    <path d="M 720 250 L 760 210 L 820 210" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="830" y="205" text-anchor="start" fill="#20d6b5">Reset Button</text>
    
    <path d="M 830 360 L 890 360 L 930 360" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="940" y="355" text-anchor="start" fill="#20d6b5">54 Digital I/O Pins</text>
    <text x="940" y="375" text-anchor="start" fill="rgba(255,255,255,0.5)" font-size="14">(Includes 15 PWM pins)</text>
    
    <path d="M 620 460 L 650 510 L 700 510" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="710" y="515" text-anchor="start" fill="#20d6b5">16 Analog Input Pins</text>
  </g>
</svg>"""

# 2. arduino_mega_pinout.svg
pinout_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
  <title id="title">Arduino Mega Pinout</title>
  <desc id="desc">Pinout diagram for Arduino Mega showing power, analog, digital, PWM, and Serial pins.</desc>
  <rect width="1200" height="650" fill="#071014" rx="12"/>
  {defs}
  <rect width="1200" height="650" fill="url(#grid)" rx="12"/>
  
  <text x="600" y="60" text-anchor="middle" fill="#00ffd5" font-size="32" font-family="Arial" font-weight="bold">Arduino Mega Pinout Diagram</text>
  
  <!-- Legends -->
  <g font-family="Arial" font-size="14" font-weight="bold">
    <rect x="50" y="80" width="120" height="25" rx="4" fill="#e74c3c"/><text x="110" y="98" text-anchor="middle" fill="#fff">Power / GND</text>
    <rect x="180" y="80" width="120" height="25" rx="4" fill="#2ecc71"/><text x="240" y="98" text-anchor="middle" fill="#fff">Analog Pins</text>
    <rect x="310" y="80" width="120" height="25" rx="4" fill="#3498db"/><text x="370" y="98" text-anchor="middle" fill="#fff">Digital I/O</text>
    <rect x="440" y="80" width="120" height="25" rx="4" fill="#9b59b6"/><text x="500" y="98" text-anchor="middle" fill="#fff">PWM (~)</text>
    <rect x="570" y="80" width="120" height="25" rx="4" fill="#e67e22"/><text x="630" y="98" text-anchor="middle" fill="#fff">Hardware Serial</text>
  </g>

  <!-- Draw Mega Center -->
  {draw_mega(600, 360, 1.15)}
  
  <g font-family="Arial" font-size="14" font-weight="bold" fill="#fff">
    <!-- Top Pins (Digital 0-13, I2C) -->
    <!-- Just drawing group brackets to keep it clean instead of 54 individual labels -->
    
    <!-- Top left bracket for PWM / Digital (D0-D13) -->
    <path d="M 520 240 L 520 220 L 720 220 L 720 240" fill="none" stroke="#9b59b6" stroke-width="2"/>
    <rect x="560" y="190" width="120" height="24" rx="4" fill="#9b59b6"/>
    <text x="620" y="207" text-anchor="middle">PWM (D2-D13)</text>
    
    <!-- I2C/SDA SCL Top right -->
    <path d="M 730 240 L 730 220 L 760 220 L 760 240" fill="none" stroke="#f1c40f" stroke-width="2"/>
    <rect x="780" y="190" width="80" height="24" rx="4" fill="#f1c40f"/>
    <text x="820" y="207" text-anchor="middle" fill="#000">I2C (SDA/SCL)</text>

    <!-- Right Side Double Header (D22 - D53) -->
    <path d="M 820 260 L 840 260 L 840 450 L 820 450" fill="none" stroke="#3498db" stroke-width="2"/>
    <rect x="860" y="340" width="140" height="24" rx="4" fill="#3498db"/>
    <text x="930" y="357" text-anchor="middle">Digital I/O (D22-D53)</text>
    
    <!-- Serial Ports (TX0/RX0, TX1/RX1, TX2/RX2, TX3/RX3) -->
    <!-- Highlight near bottom right of the double header or top right -->
    <!-- Serial 1,2,3 are at D14-D19 on Mega -->
    <path d="M 780 260 L 800 260 L 800 320 L 780 320" fill="none" stroke="#e67e22" stroke-width="2"/>
    <rect x="860" y="280" width="140" height="24" rx="4" fill="#e67e22"/>
    <text x="930" y="297" text-anchor="middle">Serial 1, 2, 3</text>

    <!-- Bottom Left Power Pins -->
    <path d="M 440 470 L 440 490 L 530 490 L 530 470" fill="none" stroke="#e74c3c" stroke-width="2"/>
    <rect x="420" y="510" width="130" height="24" rx="4" fill="#e74c3c"/>
    <text x="485" y="527" text-anchor="middle">Power (5V, 3V3, VIN)</text>

    <!-- Bottom Right Analog Pins -->
    <path d="M 540 470 L 540 490 L 740 490 L 740 470" fill="none" stroke="#2ecc71" stroke-width="2"/>
    <rect x="580" y="510" width="130" height="24" rx="4" fill="#2ecc71"/>
    <text x="645" y="527" text-anchor="middle">Analog (A0 - A15)</text>

    <!-- Left side callouts for ICSP & USB -->
    <rect x="200" y="240" width="100" height="24" rx="4" fill="#888"/>
    <text x="250" y="257" text-anchor="middle">USB Type-B</text>
    <line x1="300" y1="252" x2="360" y2="252" stroke="#888" stroke-width="2"/>
  </g>
</svg>"""

# 3. arduino_mega_components.svg
components_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
  <title id="title">Arduino Mega Component Connections</title>
  <desc id="desc">Illustration showing an Arduino Mega connected to an LCD display, a motor driver, and multiple sensors simultaneously.</desc>
  <rect width="1200" height="650" fill="#071014" rx="12"/>
  {defs}
  <rect width="1200" height="650" fill="url(#grid)" rx="12"/>
  
  <text x="600" y="70" text-anchor="middle" fill="#00ffd5" font-size="32" font-family="Arial" font-weight="bold">Multiple Component Connections</text>
  <text x="600" y="110" text-anchor="middle" fill="rgba(246, 251, 255, 0.72)" font-size="18" font-family="Arial">The Mega's 54 digital pins and 16 analog pins make it perfect for complex, multi-component systems.</text>

  <!-- Draw Mega in Center -->
  {draw_mega(600, 360, 0.85)}

  <!-- Draw LCD Display (Top Left) -->
  <g transform="translate(250, 180)">
    <rect x="-100" y="-40" width="200" height="80" rx="4" fill="#0e5a26" stroke="#004d1a" stroke-width="3"/>
    <rect x="-80" y="-30" width="160" height="60" fill="#8bc34a"/>
    <text x="0" y="5" text-anchor="middle" fill="#1b5e20" font-family="monospace" font-size="20" font-weight="bold">I2C LCD 16x2</text>
    <!-- I2C Pins -->
    <circle cx="80" cy="-20" r="3" fill="#ffd700"/>
    <circle cx="80" cy="-10" r="3" fill="#ffd700"/>
    <circle cx="80" cy="0" r="3" fill="#ffd700"/>
    <circle cx="80" cy="10" r="3" fill="#ffd700"/>
  </g>
  <!-- Wiring LCD to Mega -->
  <path d="M 330 180 C 400 180, 500 200, 550 280" fill="none" stroke="#f1c40f" stroke-width="3" stroke-dasharray="8,4"/>
  
  <!-- Draw Motor Driver L298N (Bottom Left) -->
  <g transform="translate(250, 500)">
    <rect x="-60" y="-50" width="120" height="100" rx="4" fill="#c0392b" stroke="#922b21" stroke-width="3"/>
    <rect x="-40" y="-30" width="80" height="60" fill="#111" rx="2"/>
    <rect x="-70" y="-20" width="10" height="40" fill="#fff" stroke="#999"/> <!-- Motor A -->
    <rect x="60" y="-20" width="10" height="40" fill="#fff" stroke="#999"/> <!-- Motor B -->
    <text x="0" y="5" text-anchor="middle" fill="#fff" font-family="Arial" font-size="16" font-weight="bold">L298N</text>
    <text x="0" y="20" text-anchor="middle" fill="#fff" font-family="Arial" font-size="10">Motor Driver</text>
  </g>
  <!-- Wiring Motor Driver to Mega (PWM pins) -->
  <path d="M 310 480 C 400 480, 500 450, 530 380" fill="none" stroke="#9b59b6" stroke-width="3" stroke-dasharray="8,4"/>

  <!-- Draw RFID Module (Top Right) -->
  <g transform="translate(950, 180)">
    <rect x="-60" y="-80" width="120" height="160" rx="8" fill="#2980b9" stroke="#1c5980" stroke-width="3"/>
    <circle cx="0" cy="-20" r="40" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="10,5" opacity="0.6"/>
    <text x="0" y="60" text-anchor="middle" fill="#fff" font-family="Arial" font-size="16" font-weight="bold">RC522 RFID</text>
    <!-- SPI Pins -->
    <rect x="-50" y="65" width="100" height="10" fill="#111"/>
  </g>
  <!-- Wiring RFID to Mega (SPI pins) -->
  <path d="M 890 240 C 820 240, 750 250, 700 290" fill="none" stroke="#3498db" stroke-width="3" stroke-dasharray="8,4"/>

  <!-- Draw Sensor Array (Bottom Right) -->
  <g transform="translate(950, 480)">
    <!-- Gas Sensor -->
    <rect x="-80" y="-40" width="60" height="60" rx="30" fill="#bdc3c7" stroke="#7f8c8d" stroke-width="4"/>
    <circle cx="-50" cy="-10" r="15" fill="#ecf0f1"/>
    <!-- Temperature Sensor -->
    <rect x="20" y="-40" width="60" height="60" rx="4" fill="#34495e" stroke="#2c3e50" stroke-width="3"/>
    <rect x="40" y="-20" width="20" height="20" fill="#e74c3c" rx="10"/>
    <text x="-50" y="40" text-anchor="middle" fill="#fff" font-family="Arial" font-size="12">Gas (A0)</text>
    <text x="50" y="40" text-anchor="middle" fill="#fff" font-family="Arial" font-size="12">Temp (A1)</text>
  </g>
  <!-- Wiring Sensors to Mega (Analog pins) -->
  <path d="M 870 460 C 800 460, 700 450, 650 430" fill="none" stroke="#2ecc71" stroke-width="3" stroke-dasharray="8,4"/>

  <!-- Annotations -->
  <rect x="300" y="570" width="600" height="40" fill="rgba(32, 214, 181, 0.08)" rx="6" stroke="rgba(32, 214, 181, 0.2)" stroke-width="1"/>
  <text x="600" y="595" text-anchor="middle" fill="#20d6b5" font-family="Arial" font-size="16" font-weight="bold">Mega handles I2C, SPI, multiple PWM motors, and Analog Sensors simultaneously.</text>
</svg>"""

with open(os.path.join(image_dir, "arduino_mega_board.svg"), "w", encoding="utf-8") as f:
    f.write(board_svg)

with open(os.path.join(image_dir, "arduino_mega_pinout_diagram.svg"), "w", encoding="utf-8") as f:
    f.write(pinout_svg)

with open(os.path.join(image_dir, "arduino_mega_components.svg"), "w", encoding="utf-8") as f:
    f.write(components_svg)

print("Mega SVGs generated successfully!")
