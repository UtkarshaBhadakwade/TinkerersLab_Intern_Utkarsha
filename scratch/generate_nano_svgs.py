import os

image_dir = r"c:\Users\hp\OneDrive\Desktop\TinkeresLab\image"
os.makedirs(image_dir, exist_ok=True)

# Common definitions and styles
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

# Draw Nano Board Function
def draw_nano(x, y, scale=1.0):
    # Width: 18mm -> ~180px, Height: 45mm -> ~450px
    w = 180 * scale
    h = 450 * scale
    
    board = f"""
    <g transform="translate({x}, {y}) scale({scale})">
        <!-- Board base -->
        <rect x="-90" y="-225" width="180" height="450" rx="10" fill="url(#boardGrad)" stroke="#00979d" stroke-width="2"/>
        
        <!-- USB Mini Port -->
        <rect x="-35" y="-235" width="70" height="40" rx="3" fill="#c0c0c0" stroke="#888" stroke-width="2"/>
        <rect x="-25" y="-230" width="50" height="15" fill="#444" rx="2"/>
        
        <!-- Reset Button -->
        <rect x="-15" y="-180" width="30" height="20" rx="2" fill="#dcdcdc" stroke="#999" stroke-width="1"/>
        <circle cx="0" cy="-170" r="5" fill="#e74c3c"/>
        
        <!-- ICSP Header -->
        <rect x="-15" y="160" width="30" height="45" fill="#222" rx="2"/>
        <!-- 6 pins -->
        <circle cx="-7" cy="167.5" r="3" fill="#ffd700"/><circle cx="7" cy="167.5" r="3" fill="#ffd700"/>
        <circle cx="-7" cy="182.5" r="3" fill="#ffd700"/><circle cx="7" cy="182.5" r="3" fill="#ffd700"/>
        <circle cx="-7" cy="197.5" r="3" fill="#ffd700"/><circle cx="7" cy="197.5" r="3" fill="#ffd700"/>

        <!-- ATmega328P Chip -->
        <rect x="-30" y="-40" width="60" height="60" rx="4" fill="url(#chipGrad)" stroke="#444" stroke-width="1"/>
        <!-- Chip pins -->
        <rect x="-35" y="-30" width="5" height="40" fill="#bbb"/>
        <rect x="30" y="-30" width="5" height="40" fill="#bbb"/>
        <text x="0" y="-15" fill="#fff" font-family="monospace" font-size="6" text-anchor="middle" opacity="0.6">ATMEGA</text>
        <text x="0" y="-5" fill="#fff" font-family="monospace" font-size="6" text-anchor="middle" opacity="0.6">328P-AU</text>
        
        <!-- CH340 / USB UART Chip -->
        <rect x="-15" y="80" width="30" height="40" rx="2" fill="#222" stroke="#111" stroke-width="1"/>
        
        <!-- Side Pins (15 on each side) -->
    """
    
    # Left pins (D13 to TX1)
    for i in range(15):
        py = -200 + (i * 26.5)
        board += f'<circle cx="-75" cy="{py}" r="5" fill="#ffd700" stroke="#b8860b" stroke-width="1"/>'
        board += f'<circle cx="-75" cy="{py}" r="2" fill="#222"/>'
        
    # Right pins (D12 to VIN)
    for i in range(15):
        py = -200 + (i * 26.5)
        board += f'<circle cx="75" cy="{py}" r="5" fill="#ffd700" stroke="#b8860b" stroke-width="1"/>'
        board += f'<circle cx="75" cy="{py}" r="2" fill="#222"/>'
        
    board += "</g>"
    return board

# 1. arduino_nano_board.svg
board_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
  <title id="title">Arduino Nano Board</title>
  <desc id="desc">Vector illustration of Arduino Nano microcontroller board.</desc>
  <rect width="1200" height="650" fill="#071014" rx="12"/>
  {defs}
  <rect width="1200" height="650" fill="url(#grid)" rx="12"/>
  
  <text x="600" y="80" text-anchor="middle" fill="#00ffd5" font-size="36" font-family="Arial" font-weight="bold">Arduino Nano Overview</text>
  <text x="600" y="120" text-anchor="middle" fill="rgba(246, 251, 255, 0.72)" font-size="18" font-family="Arial">A compact, breadboard-friendly microcontroller board based on the ATmega328P.</text>
  
  <!-- Draw Nano -->
  {draw_nano(600, 370, 0.9)}

  <!-- Callouts -->
  <g font-family="Arial" font-size="16" fill="#f6fbff">
    <path d="M 540 160 L 450 120 L 400 120" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="390" y="125" text-anchor="end" fill="#20d6b5">Mini USB Port</text>
    
    <path d="M 540 360 L 450 360 L 400 360" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="390" y="365" text-anchor="end" fill="#20d6b5">ATmega328P Microcontroller</text>
    <text x="390" y="385" text-anchor="end" fill="rgba(255,255,255,0.5)" font-size="14">32 KB Flash, 2 KB SRAM</text>

    <path d="M 540 200 L 450 240 L 400 240" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="390" y="245" text-anchor="end" fill="#20d6b5">Reset Button</text>
    
    <path d="M 660 540 L 750 560 L 800 560" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="810" y="565" text-anchor="start" fill="#20d6b5">ICSP Header</text>
    
    <path d="M 680 370 L 750 370 L 800 370" fill="none" stroke="#20d6b5" stroke-width="2"/>
    <text x="810" y="375" text-anchor="start" fill="#20d6b5">30 Header Pins</text>
    <text x="810" y="395" text-anchor="start" fill="rgba(255,255,255,0.5)" font-size="14">Analog, Digital, PWM &amp; Power</text>
  </g>
</svg>"""

# 2. arduino_nano_pinout.svg
pinout_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
  <title id="title">Arduino Nano Pinout</title>
  <desc id="desc">Pinout diagram for Arduino Nano showing power, analog, digital, and PWM pins.</desc>
  <rect width="1200" height="650" fill="#071014" rx="12"/>
  {defs}
  <rect width="1200" height="650" fill="url(#grid)" rx="12"/>
  
  <text x="600" y="60" text-anchor="middle" fill="#00ffd5" font-size="32" font-family="Arial" font-weight="bold">Arduino Nano Pinout Diagram</text>
  
  <!-- Draw Nano Center -->
  {draw_nano(600, 360, 0.95)}
  
  <!-- Legends -->
  <g font-family="Arial" font-size="14" font-weight="bold">
    <rect x="50" y="80" width="120" height="25" rx="4" fill="#e74c3c"/><text x="110" y="98" text-anchor="middle" fill="#fff">Power / GND</text>
    <rect x="180" y="80" width="120" height="25" rx="4" fill="#2ecc71"/><text x="240" y="98" text-anchor="middle" fill="#fff">Analog Pins</text>
    <rect x="310" y="80" width="120" height="25" rx="4" fill="#3498db"/><text x="370" y="98" text-anchor="middle" fill="#fff">Digital I/O</text>
    <rect x="440" y="80" width="120" height="25" rx="4" fill="#9b59b6"/><text x="500" y="98" text-anchor="middle" fill="#fff">PWM (~)</text>
    <rect x="570" y="80" width="120" height="25" rx="4" fill="#e67e22"/><text x="630" y="98" text-anchor="middle" fill="#fff">UART (TX/RX)</text>
  </g>

  <!-- Left Side Pins (from top to bottom D13 to TX1) -->
  <g font-family="monospace" font-size="14" font-weight="bold" fill="#fff">
    <!-- TX1/D1, RX0/D0, RST, GND, D2, D3~, D4, D5~, D6~, D7, D8, D9~, D10~, D11~, D12 (Actually standard Nano pinout from top left is D13, 3V3, REF, A0-A7, 5V, RST, GND, VIN, wait. Let me do a standard pinout text list) -->
    <!-- Let's map them out explicitly for Arduino Nano:
         Left side (top down, USB at top): TX1, RX0, RST, GND, D2, D3~, D4, D5~, D6~, D7, D8, D9~, D10~, D11~, D12
         Wait, USB at top: Left side is actually TX1, RX0, RST, GND, D2... D12
         Right side: D13, 3V3, AREF, A0, A1, A2, A3, A4, A5, A6, A7, 5V, RST, GND, VIN 
    -->
    <!-- Left pins: -->
    <!-- D12 --> <rect x="380" y="160" width="120" height="20" rx="3" fill="#3498db"/><text x="440" y="175" text-anchor="middle">D12 / MISO</text> <line x1="500" y1="170" x2="525" y2="170" stroke="#3498db" stroke-width="2"/>
    <!-- D11~ --> <rect x="380" y="185" width="120" height="20" rx="3" fill="#9b59b6"/><text x="440" y="200" text-anchor="middle">D11~ / MOSI</text> <line x1="500" y1="195" x2="525" y2="195" stroke="#9b59b6" stroke-width="2"/>
    <!-- D10~ --> <rect x="380" y="210" width="120" height="20" rx="3" fill="#9b59b6"/><text x="440" y="225" text-anchor="middle">D10~ / SS</text> <line x1="500" y1="220" x2="525" y2="220" stroke="#9b59b6" stroke-width="2"/>
    <!-- D9~ --> <rect x="380" y="235" width="120" height="20" rx="3" fill="#9b59b6"/><text x="440" y="250" text-anchor="middle">D9~</text> <line x1="500" y1="245" x2="525" y2="245" stroke="#9b59b6" stroke-width="2"/>
    <!-- D8 --> <rect x="380" y="260" width="120" height="20" rx="3" fill="#3498db"/><text x="440" y="275" text-anchor="middle">D8</text> <line x1="500" y1="270" x2="525" y2="270" stroke="#3498db" stroke-width="2"/>
    <!-- D7 --> <rect x="380" y="285" width="120" height="20" rx="3" fill="#3498db"/><text x="440" y="300" text-anchor="middle">D7</text> <line x1="500" y1="295" x2="525" y2="295" stroke="#3498db" stroke-width="2"/>
    <!-- D6~ --> <rect x="380" y="310" width="120" height="20" rx="3" fill="#9b59b6"/><text x="440" y="325" text-anchor="middle">D6~</text> <line x1="500" y1="320" x2="525" y2="320" stroke="#9b59b6" stroke-width="2"/>
    <!-- D5~ --> <rect x="380" y="335" width="120" height="20" rx="3" fill="#9b59b6"/><text x="440" y="350" text-anchor="middle">D5~</text> <line x1="500" y1="345" x2="525" y2="345" stroke="#9b59b6" stroke-width="2"/>
    <!-- D4 --> <rect x="380" y="360" width="120" height="20" rx="3" fill="#3498db"/><text x="440" y="375" text-anchor="middle">D4</text> <line x1="500" y1="370" x2="525" y2="370" stroke="#3498db" stroke-width="2"/>
    <!-- D3~ --> <rect x="380" y="385" width="120" height="20" rx="3" fill="#9b59b6"/><text x="440" y="400" text-anchor="middle">D3~ / INT1</text> <line x1="500" y1="395" x2="525" y2="395" stroke="#9b59b6" stroke-width="2"/>
    <!-- D2 --> <rect x="380" y="410" width="120" height="20" rx="3" fill="#3498db"/><text x="440" y="425" text-anchor="middle">D2 / INT0</text> <line x1="500" y1="420" x2="525" y2="420" stroke="#3498db" stroke-width="2"/>
    <!-- GND --> <rect x="380" y="435" width="120" height="20" rx="3" fill="#2c3e50"/><text x="440" y="450" text-anchor="middle">GND</text> <line x1="500" y1="445" x2="525" y2="445" stroke="#2c3e50" stroke-width="2"/>
    <!-- RST --> <rect x="380" y="460" width="120" height="20" rx="3" fill="#e74c3c"/><text x="440" y="475" text-anchor="middle">RST</text> <line x1="500" y1="470" x2="525" y2="470" stroke="#e74c3c" stroke-width="2"/>
    <!-- RX0 --> <rect x="380" y="485" width="120" height="20" rx="3" fill="#e67e22"/><text x="440" y="500" text-anchor="middle">RX0 / D0</text> <line x1="500" y1="495" x2="525" y2="495" stroke="#e67e22" stroke-width="2"/>
    <!-- TX1 --> <rect x="380" y="510" width="120" height="20" rx="3" fill="#e67e22"/><text x="440" y="525" text-anchor="middle">TX1 / D1</text> <line x1="500" y1="520" x2="525" y2="520" stroke="#e67e22" stroke-width="2"/>

    <!-- Right pins: -->
    <!-- D13 --> <rect x="700" y="160" width="120" height="20" rx="3" fill="#3498db"/><text x="760" y="175" text-anchor="middle">D13 / SCK</text> <line x1="675" y1="170" x2="700" y2="170" stroke="#3498db" stroke-width="2"/>
    <!-- 3V3 --> <rect x="700" y="185" width="120" height="20" rx="3" fill="#e74c3c"/><text x="760" y="200" text-anchor="middle">3V3</text> <line x1="675" y1="195" x2="700" y2="195" stroke="#e74c3c" stroke-width="2"/>
    <!-- REF --> <rect x="700" y="210" width="120" height="20" rx="3" fill="#f1c40f"/><text x="760" y="225" text-anchor="middle" fill="#000">AREF</text> <line x1="675" y1="220" x2="700" y2="220" stroke="#f1c40f" stroke-width="2"/>
    <!-- A0 --> <rect x="700" y="235" width="120" height="20" rx="3" fill="#2ecc71"/><text x="760" y="250" text-anchor="middle">A0</text> <line x1="675" y1="245" x2="700" y2="245" stroke="#2ecc71" stroke-width="2"/>
    <!-- A1 --> <rect x="700" y="260" width="120" height="20" rx="3" fill="#2ecc71"/><text x="760" y="275" text-anchor="middle">A1</text> <line x1="675" y1="270" x2="700" y2="270" stroke="#2ecc71" stroke-width="2"/>
    <!-- A2 --> <rect x="700" y="285" width="120" height="20" rx="3" fill="#2ecc71"/><text x="760" y="300" text-anchor="middle">A2</text> <line x1="675" y1="295" x2="700" y2="295" stroke="#2ecc71" stroke-width="2"/>
    <!-- A3 --> <rect x="700" y="310" width="120" height="20" rx="3" fill="#2ecc71"/><text x="760" y="325" text-anchor="middle">A3</text> <line x1="675" y1="320" x2="700" y2="320" stroke="#2ecc71" stroke-width="2"/>
    <!-- A4 --> <rect x="700" y="335" width="120" height="20" rx="3" fill="#2ecc71"/><text x="760" y="350" text-anchor="middle">A4 / SDA</text> <line x1="675" y1="345" x2="700" y2="345" stroke="#2ecc71" stroke-width="2"/>
    <!-- A5 --> <rect x="700" y="360" width="120" height="20" rx="3" fill="#2ecc71"/><text x="760" y="375" text-anchor="middle">A5 / SCL</text> <line x1="675" y1="370" x2="700" y2="370" stroke="#2ecc71" stroke-width="2"/>
    <!-- A6 --> <rect x="700" y="385" width="120" height="20" rx="3" fill="#2ecc71"/><text x="760" y="400" text-anchor="middle">A6</text> <line x1="675" y1="395" x2="700" y2="395" stroke="#2ecc71" stroke-width="2"/>
    <!-- A7 --> <rect x="700" y="410" width="120" height="20" rx="3" fill="#2ecc71"/><text x="760" y="425" text-anchor="middle">A7</text> <line x1="675" y1="420" x2="700" y2="420" stroke="#2ecc71" stroke-width="2"/>
    <!-- 5V --> <rect x="700" y="435" width="120" height="20" rx="3" fill="#e74c3c"/><text x="760" y="450" text-anchor="middle">5V</text> <line x1="675" y1="445" x2="700" y2="445" stroke="#e74c3c" stroke-width="2"/>
    <!-- RST --> <rect x="700" y="460" width="120" height="20" rx="3" fill="#e74c3c"/><text x="760" y="475" text-anchor="middle">RST</text> <line x1="675" y1="470" x2="700" y2="470" stroke="#e74c3c" stroke-width="2"/>
    <!-- GND --> <rect x="700" y="485" width="120" height="20" rx="3" fill="#2c3e50"/><text x="760" y="500" text-anchor="middle">GND</text> <line x1="675" y1="495" x2="700" y2="495" stroke="#2c3e50" stroke-width="2"/>
    <!-- VIN --> <rect x="700" y="510" width="120" height="20" rx="3" fill="#e74c3c"/><text x="760" y="525" text-anchor="middle">VIN</text> <line x1="675" y1="520" x2="700" y2="520" stroke="#e74c3c" stroke-width="2"/>
  </g>
</svg>"""

# 3. arduino_nano_breadboard.svg
breadboard_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
  <title id="title">Arduino Nano on Breadboard</title>
  <desc id="desc">Illustration showing an Arduino Nano plugged into a breadboard with a basic LED circuit.</desc>
  <rect width="1200" height="650" fill="#071014" rx="12"/>
  {defs}
  <rect width="1200" height="650" fill="url(#grid)" rx="12"/>
  
  <text x="600" y="70" text-anchor="middle" fill="#00ffd5" font-size="32" font-family="Arial" font-weight="bold">Breadboard Circuit Reference</text>
  <text x="600" y="110" text-anchor="middle" fill="rgba(246, 251, 255, 0.72)" font-size="18" font-family="Arial">Arduino Nano is perfectly sized to fit directly onto a standard breadboard.</text>

  <!-- Breadboard -->
  <g transform="translate(600, 360)">
    <!-- Base -->
    <rect x="-350" y="-220" width="700" height="440" rx="15" fill="#e6e6e6" stroke="#ccc" stroke-width="4"/>
    <rect x="-345" y="-215" width="690" height="430" rx="12" fill="#fafafa"/>
    
    <!-- Center divider -->
    <rect x="-320" y="-10" width="640" height="20" fill="#ddd" rx="4"/>
    
    <!-- Holes -->
    <!-- Left Power Rail -->
    <line x1="-320" y1="-200" x2="-320" y2="200" stroke="#e74c3c" stroke-width="2"/>
    <line x1="-300" y1="-200" x2="-300" y2="200" stroke="#3498db" stroke-width="2"/>
    
    <!-- Right Power Rail -->
    <line x1="300" y1="-200" x2="300" y2="200" stroke="#e74c3c" stroke-width="2"/>
    <line x1="320" y1="-200" x2="320" y2="200" stroke="#3498db" stroke-width="2"/>
    
    <!-- Just draw an abstract matrix of holes for simplicity instead of individually grouping all -->
    <g fill="#444">
    <!-- Too many holes = big svg, we just draw lines of holes -->
    </g>
    <!-- Simplified breadboard hole matrix with paths -->
  </g>
  
  <!-- Since generating 3000 dots makes the SVG huge, I will use a pattern for the breadboard holes -->
  <defs>
    <pattern id="bbHoles" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="3" fill="#444"/>
    </pattern>
  </defs>
  
  <!-- Apply holes to breadboard -->
  <rect x="360" y="160" width="480" height="130" fill="url(#bbHoles)"/>
  <rect x="360" y="370" width="480" height="130" fill="url(#bbHoles)"/>
  
  <rect x="260" y="160" width="40" height="400" fill="url(#bbHoles)"/>
  <rect x="900" y="160" width="40" height="400" fill="url(#bbHoles)"/>

  <!-- Draw Nano horizontally inserted across center divider -->
  <g transform="translate(600, 360) rotate(-90)">
    {draw_nano(0, 0, 0.85)}
  </g>

  <!-- Wiring and LED to show it's a circuit -->
  <!-- Red wire from D13 to LED -->
  <path d="M 660 300 C 660 250, 750 250, 750 220" fill="none" stroke="#e74c3c" stroke-width="4"/>
  <!-- Resistor from LED to GND -->
  <path d="M 770 220 L 780 220 L 785 210 L 795 230 L 805 210 L 815 230 L 820 220 L 840 220" fill="none" stroke="#d35400" stroke-width="3"/>
  <rect x="785" y="215" width="30" height="10" rx="3" fill="#e4c59b"/>
  <!-- LED -->
  <path d="M 740 210 Q 760 190 780 210 Z" fill="#ff4d4d"/>
  <circle cx="760" cy="210" r="15" fill="#ff4d4d" opacity="0.8"/>
  <rect x="750" y="210" width="20" height="10" fill="#cc0000"/>
  
  <!-- Black wire to GND rail -->
  <path d="M 840 220 C 840 280, 890 280, 910 250" fill="none" stroke="#222" stroke-width="4"/>
  
  <!-- Annotation -->
  <rect x="700" y="120" width="250" height="60" rx="6" fill="#132b3f" stroke="#4da3ff" stroke-width="1"/>
  <text x="825" y="145" text-anchor="middle" fill="#f6fbff" font-family="Arial" font-size="14">Basic LED Circuit setup</text>
  <text x="825" y="165" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-family="Arial" font-size="12">Shows standard spacing usage</text>

</svg>"""

with open(os.path.join(image_dir, "arduino_nano_board.svg"), "w", encoding="utf-8") as f:
    f.write(board_svg)

with open(os.path.join(image_dir, "arduino_nano_pinout_diagram.svg"), "w", encoding="utf-8") as f:
    f.write(pinout_svg)

with open(os.path.join(image_dir, "arduino_nano_breadboard.svg"), "w", encoding="utf-8") as f:
    f.write(breadboard_svg)

print("Nano SVGs generated successfully!")
