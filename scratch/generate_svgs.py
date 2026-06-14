import os

image_dir = r"c:\Users\hp\OneDrive\Desktop\TinkeresLab\image"
os.makedirs(image_dir, exist_ok=True)

# ----------------- STEP 2 SVG -----------------
step2_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
  <title id="title">Step 2: Base Plate Sketch and Extrusion</title>
  <desc id="desc">Isometric diagram illustrating the ground plane rectangle sketch and extruded base plate in Autodesk Fusion.</desc>
  <rect width="1200" height="650" fill="#071014" rx="12"/>
  <!-- Decorative Grid Overlay -->
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255, 255, 255, 0.03)" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="1200" height="650" fill="url(#grid)" rx="12"/>
  
  <text x="600" y="70" text-anchor="middle" fill="#f6fbff" font-size="36" font-family="Arial" font-weight="bold">Step 2: Base Plate Sketch &amp; Extrusion</text>
  <text x="600" y="110" text-anchor="middle" fill="rgba(246, 251, 255, 0.72)" font-size="18" font-family="Arial">Sketch center rectangle (120 x 75 mm) on XY plane and extrude 5 mm upward</text>

  <!-- 3D Coordinate Axis Legend -->
  <g transform="translate(100, 520)" stroke-width="2" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">
    <line x1="0" y1="0" x2="60" y2="30" stroke="#4da3ff" /> <!-- X axis -->
    <line x1="0" y1="0" x2="-60" y2="30" stroke="#ffffd1" /> <!-- Y axis -->
    <line x1="0" y1="0" x2="0" y2="-70" stroke="#20d6b5" /> <!-- Z axis -->
    <text x="70" y="40" fill="#4da3ff">X (Width)</text>
    <text x="-75" y="40" fill="#ffffd1">Y (Depth)</text>
    <text x="0" y="-80" fill="#20d6b5">Z (Height)</text>
    <circle cx="0" cy="0" r="4" fill="#f6fbff"/>
  </g>

  <!-- Ground Plane (XY grid representation) -->
  <path d="M 600 130 L 950 305 L 600 480 L 250 305 Z" fill="none" stroke="rgba(77, 163, 255, 0.1)" stroke-width="2"/>
  <path d="M 600 130 L 600 480" fill="none" stroke="rgba(77, 163, 255, 0.05)" stroke-width="1"/>
  <path d="M 250 305 L 950 305" fill="none" stroke="rgba(77, 163, 255, 0.05)" stroke-width="1"/>

  <!-- Base Plate Geometry -->
  <!-- Bottom Face -->
  <polygon points="541.5,183.75 853.3,333.75 658.46,476.25 346.7,296.25" fill="#0f1f2d" opacity="0.6"/>
  <!-- Extrusion Guide Lines -->
  <line x1="541.5" y1="183.75" x2="541.5" y2="153.75" stroke="#20d6b5" stroke-dasharray="4,4" stroke-width="2"/>
  <line x1="853.3" y1="333.75" x2="853.3" y2="303.75" stroke="#20d6b5" stroke-dasharray="4,4" stroke-width="2"/>
  <line x1="346.7" y1="296.25" x2="346.7" y2="266.25" stroke="#20d6b5" stroke-dasharray="4,4" stroke-width="2"/>
  <line x1="658.46" y1="476.25" x2="658.46" y2="446.25" stroke="#20d6b5" stroke-width="2"/>

  <!-- Extrusion Direction Arrows -->
  <g stroke="#20d6b5" stroke-width="3" fill="none">
    <path d="M 400 380 L 400 320"/>
    <path d="M 395 330 L 400 320 L 405 330"/>
    <path d="M 800 410 L 800 350"/>
    <path d="M 795 360 L 800 350 L 805 360"/>
  </g>
  <text x="420" y="355" fill="#20d6b5" font-family="Arial" font-size="16" font-weight="bold">Extrude (Z): 5 mm</text>

  <!-- Top Face (Final Extruded Shape) -->
  <polygon points="541.5,153.75 853.3,303.75 658.46,446.25 346.7,266.25" fill="#132b3f" stroke="#4da3ff" stroke-width="3"/>
  
  <!-- Left Side Face -->
  <polygon points="346.7,266.25 658.46,446.25 658.46,476.25 346.7,296.25" fill="#0e2132" stroke="#4da3ff" stroke-width="2"/>
  
  <!-- Right Side Face -->
  <polygon points="658.46,446.25 853.3,303.75 853.3,333.75 658.46,476.25" fill="#091825" stroke="#4da3ff" stroke-width="2"/>

  <!-- Dimensions Annotations -->
  <!-- Width: 120 mm -->
  <g fill="#f6fbff" font-family="Arial" font-size="15" font-weight="bold">
    <line x1="326.7" y1="286.25" x2="638.46" y2="466.25" stroke="#ffd166" stroke-width="2"/>
    <line x1="326.7" y1="276.25" x2="326.7" y2="296.25" stroke="#ffd166" stroke-width="2"/>
    <line x1="638.46" y1="456.25" x2="638.46" y2="476.25" stroke="#ffd166" stroke-width="2"/>
    <rect x="440" y="355" width="80" height="26" fill="#071014" rx="4"/>
    <text x="480" y="373" text-anchor="middle" fill="#ffd166">120 mm</text>
  </g>

  <!-- Depth: 75 mm -->
  <g fill="#f6fbff" font-family="Arial" font-size="15" font-weight="bold">
    <line x1="678.46" y1="466.25" x2="873.3" y2="323.75" stroke="#ffd166" stroke-width="2"/>
    <line x1="678.46" y1="456.25" x2="678.46" y2="476.25" stroke="#ffd166" stroke-width="2"/>
    <line x1="873.3" y1="313.75" x2="873.3" y2="333.75" stroke="#ffd166" stroke-width="2"/>
    <rect x="745" y="375" width="70" height="26" fill="#071014" rx="4"/>
    <text x="780" y="393" text-anchor="middle" fill="#ffd166">75 mm</text>
  </g>

  <!-- Thickness: 5 mm -->
  <g fill="#f6fbff" font-family="Arial" font-size="14">
    <line x1="883.3" y1="303.75" x2="883.3" y2="333.75" stroke="#ffd166" stroke-width="1.5"/>
    <line x1="878.3" y1="303.75" x2="888.3" y2="303.75" stroke="#ffd166" stroke-width="1.5"/>
    <line x1="878.3" y1="333.75" x2="888.3" y2="333.75" stroke="#ffd166" stroke-width="1.5"/>
    <text x="900" y="323" fill="#ffd166" font-weight="bold">5 mm</text>
  </g>

  <rect x="250" y="550" width="700" height="40" fill="rgba(32, 214, 181, 0.08)" rx="6" stroke="rgba(32, 214, 181, 0.2)" stroke-width="1"/>
  <text x="600" y="575" text-anchor="middle" fill="#20d6b5" font-family="Arial" font-size="16" font-weight="bold">CAD Workflow: Sketch Center Rectangle → Extrude 5mm → Define Base Body</text>
</svg>"""

# ----------------- STEP 3 SVG -----------------
step3_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
  <title id="title">Step 3: Base Text Extrusion</title>
  <desc id="desc">Isometric diagram showing the base plate with the text BHADAKWADE extruded upward in Autodesk Fusion.</desc>
  <rect width="1200" height="650" fill="#071014" rx="12"/>
  <rect width="1200" height="650" fill="url(#grid)" rx="12"/>
  
  <text x="600" y="70" text-anchor="middle" fill="#f6fbff" font-size="36" font-family="Arial" font-weight="bold">Step 3: Add Raised Base Text "BHADAKWADE"</text>
  <text x="600" y="110" text-anchor="middle" fill="rgba(246, 251, 255, 0.72)" font-size="18" font-family="Arial">Sketch text on upper surface of base plate and extrude upward 2.5 mm</text>

  <!-- Base Plate (Extruded Box) -->
  <polygon points="541.5,183.75 853.3,333.75 658.46,476.25 346.7,296.25" fill="#0e2132" opacity="0.4"/>
  <polygon points="541.5,153.75 853.3,303.75 658.46,446.25 346.7,266.25" fill="#132b3f" stroke="#4da3ff" stroke-width="2"/>
  <polygon points="346.7,266.25 658.46,446.25 658.46,476.25 346.7,296.25" fill="#0e2132" stroke="#4da3ff" stroke-width="1.5"/>
  <polygon points="658.46,446.25 853.3,303.75 853.3,333.75 658.46,476.25" fill="#091825" stroke="#4da3ff" stroke-width="1.5"/>

  <!-- Text BHADAKWADE Skewed on top surface -->
  <!-- In isometric perspective, mapping flat on top surface: transform matrix -->
  <g transform="matrix(0.8660, 0.5, -0.8660, 0.5, 600, 270)">
    <!-- 3D Effect for Text: Redraw offset bottom layer in cyan/black, then front layer -->
    <text x="-140" y="82" fill="#0b1714" font-family="Impact, Arial Black, Arial" font-size="34" font-weight="bold" letter-spacing="4">BHADAKWADE</text>
    <text x="-140" y="81" fill="#0b1714" font-family="Impact, Arial Black, Arial" font-size="34" font-weight="bold" letter-spacing="4">BHADAKWADE</text>
    <text x="-140" y="80" fill="#20d6b5" font-family="Impact, Arial Black, Arial" font-size="34" font-weight="bold" letter-spacing="4">BHADAKWADE</text>
  </g>

  <!-- Extrusion thickness annotation for Text -->
  <g stroke="#20d6b5" stroke-width="2" fill="none">
    <path d="M 525 385 L 525 360"/>
    <path d="M 521 368 L 525 360 L 529 368"/>
    <path d="M 675 422 L 675 397"/>
    <path d="M 671 405 L 675 397 L 679 405"/>
  </g>
  <text x="440" y="375" fill="#20d6b5" font-family="Arial" font-size="15" font-weight="bold" text-anchor="middle">Extrude Text: 2.5 mm</text>

  <!-- Dimensions Annotations -->
  <g fill="#f6fbff" font-family="Arial" font-size="15" font-weight="bold" text-anchor="middle">
    <!-- Font Height: 8 mm -->
    <line x1="710" y1="275" x2="775" y2="310" stroke="#ffd166" stroke-width="1.5"/>
    <line x1="705" y1="280" x2="715" y2="270" stroke="#ffd166" stroke-width="1.5"/>
    <line x1="770" y1="315" x2="780" y2="305" stroke="#ffd166" stroke-width="1.5"/>
    <text x="770" y="270" fill="#ffd166">Text Height: 8 mm</text>
  </g>

  <rect x="250" y="550" width="700" height="40" fill="rgba(32, 214, 181, 0.08)" rx="6" stroke="rgba(32, 214, 181, 0.2)" stroke-width="1"/>
  <text x="600" y="575" text-anchor="middle" fill="#20d6b5" font-family="Arial" font-size="16" font-weight="bold">CAD Workflow: Top Face sketch → Text tool → Enter "BHADAKWADE" → Extrude Join</text>
</svg>"""

# ----------------- STEP 4 SVG -----------------
step4_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
  <title id="title">Step 4: Curved Support Columns Sketch</title>
  <desc id="desc">Side profile sketch of the curved support columns showing spline curve, 75-degree angle, and thickness.</desc>
  <rect width="1200" height="650" fill="#071014" rx="12"/>
  <rect width="1200" height="650" fill="url(#grid)" rx="12"/>
  
  <text x="600" y="70" text-anchor="middle" fill="#f6fbff" font-size="36" font-family="Arial" font-weight="bold">Step 4: Design the Curved Support Columns</text>
  <text x="600" y="110" text-anchor="middle" fill="rgba(246, 251, 255, 0.72)" font-size="18" font-family="Arial">Sketch organic support columns on vertical YZ plane using Fit Point Spline and extrude</text>

  <!-- Side View Representation (YZ Plane Projection) -->
  <!-- Base Plate Side Profile (75 mm depth x 5 mm thickness) -->
  <!-- Scale: 1 mm = 6 pixels -->
  <g transform="translate(180, 0)">
    <!-- Grid ground axis line -->
    <line x1="50" y1="480" x2="800" y2="480" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>
    <text x="780" y="472" fill="rgba(255,255,255,0.4)" font-family="Arial" font-size="14">Y (Depth)</text>
    <line x1="100" y1="130" x2="100" y2="520" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>
    <text x="115" y="145" fill="rgba(255,255,255,0.4)" font-family="Arial" font-size="14">Z (Height)</text>

    <!-- Base Plate -->
    <!-- Front is to the right (y = 75mm * 6 = 450px from back, let back be at y = 200px. So front is at y = 650px) -->
    <rect x="200" y="450" width="450" height="30" fill="#132b3f" stroke="#4da3ff" stroke-width="3" rx="2"/>
    <text x="425" y="470" fill="#f6fbff" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Base Plate (Side Profile)</text>

    <!-- Spline Curve Sketch (Support columns) -->
    <!-- Back profile: starts at y = 240, z = 450 (bottom). Curves upward and backward (to the left) -->
    <!-- Spline points: P1(240, 450), P2(220, 360), P3(190, 270), P4(175, 170) -->
    <!-- Front profile offset by 6 mm * 6 = 36 px: Q1(276, 450), Q2(256, 360), Q3(226, 270), Q4(211, 170) -->
    <!-- Closed sketch loop -->
    <path d="M 240 450 C 240 370, 210 290, 175 170 L 211 170 C 246 290, 276 370, 276 450 Z" 
          fill="rgba(32, 214, 181, 0.12)" stroke="#20d6b5" stroke-width="4" stroke-linecap="round"/>

    <!-- Highlight Spline Control Points (Fit Points) -->
    <circle cx="240" cy="450" r="5" fill="#ffd166" stroke="#071014" stroke-width="2"/>
    <circle cx="222" cy="350" r="5" fill="#ffd166" stroke="#071014" stroke-width="2"/>
    <circle cx="195" cy="250" r="5" fill="#ffd166" stroke="#071014" stroke-width="2"/>
    <circle cx="175" cy="170" r="5" fill="#ffd166" stroke="#071014" stroke-width="2"/>

    <!-- Dimension: Column Thickness 6 mm -->
    <g fill="#ffd166" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">
      <line x1="175" y1="150" x2="211" y2="150" stroke="#ffd166" stroke-width="1.5"/>
      <line x1="175" y1="145" x2="175" y2="155" stroke="#ffd166" stroke-width="1.5"/>
      <line x1="211" y1="145" x2="211" y2="155" stroke="#ffd166" stroke-width="1.5"/>
      <text x="193" y="138">6 mm</text>
    </g>

    <!-- Angle Dimension: 75° Slant Angle -->
    <!-- Angle line from back point to top point -->
    <line x1="240" y1="450" x2="165" y2="170" stroke="rgba(255, 209, 102, 0.4)" stroke-dasharray="4,4" stroke-width="1.5"/>
    <path d="M 320 450 A 80 80 0 0 0 300 376" fill="none" stroke="#ffd166" stroke-width="2"/>
    <text x="330" y="415" fill="#ffd166" font-family="Arial" font-size="15" font-weight="bold">~75° Slant</text>
  </g>

  <rect x="250" y="550" width="700" height="40" fill="rgba(32, 214, 181, 0.08)" rx="6" stroke="rgba(32, 214, 181, 0.2)" stroke-width="1"/>
  <text x="600" y="575" text-anchor="middle" fill="#20d6b5" font-family="Arial" font-size="16" font-weight="bold">CAD Workflow: Sketch on YZ plane → Fit Point Spline → Offset 6mm → Extrude Symmetric</text>
</svg>"""

# ----------------- STEP 5 SVG -----------------
step5_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
  <title id="title">Step 5: Angled Standing Letters Sketch and Extrusion</title>
  <desc id="desc">Isometric rendering showing the completed phone stand model with angled standing letters UTKARSHA merged into the support columns.</desc>
  <rect width="1200" height="650" fill="#071014" rx="12"/>
  <rect width="1200" height="650" fill="url(#grid)" rx="12"/>
  
  <text x="600" y="70" text-anchor="middle" fill="#f6fbff" font-size="36" font-family="Arial" font-weight="bold">Step 5: Sketch &amp; Extrude "UTKARSHA" Letters</text>
  <text x="600" y="110" text-anchor="middle" fill="rgba(246, 251, 255, 0.72)" font-size="18" font-family="Arial">Create an angled construction plane parallel to support columns and extrude letters 10 mm</text>

  <!-- Complete Stand Assembly in Isometric -->
  <!-- Base Plate (Extruded Box) -->
  <polygon points="541.5,183.75 853.3,333.75 658.46,476.25 346.7,296.25" fill="#0e2132" opacity="0.3"/>
  <polygon points="346.7,296.25 658.46,476.25 658.46,446.25 346.7,266.25" fill="#0e2132" stroke="#4da3ff" stroke-width="1.5" stroke-opacity="0.4"/>
  <polygon points="658.46,446.25 853.3,303.75 853.3,333.75 658.46,476.25" fill="#091825" stroke="#4da3ff" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Base Text BHADAKWADE (Low Opacity) -->
  <g transform="matrix(0.8660, 0.5, -0.8660, 0.5, 600, 270)" opacity="0.4">
    <text x="-140" y="80" fill="#20d6b5" font-family="Impact, Arial Black, Arial" font-size="34" font-weight="bold" letter-spacing="4">BHADAKWADE</text>
  </g>

  <!-- Curved support columns rising from the back (3D rendered representation) -->
  <!-- Back column 1 (left side) -->
  <path d="M 450 220 C 470 270, 480 320, 490 350 L 510 350 C 500 320, 490 270, 470 220 Z" fill="#132b3f" stroke="#4da3ff" stroke-width="1.5"/>
  <!-- Back column 2 (right side) -->
  <path d="M 720 330 C 740 380, 750 430, 760 460 L 780 460 C 770 430, 760 380, 740 330 Z" fill="#132b3f" stroke="#4da3ff" stroke-width="1.5"/>

  <!-- Angled Construction Plane (Drawn as a semi-transparent colored plane) -->
  <polygon points="380,180 820,380 750,220 310,20" fill="rgba(255, 209, 102, 0.08)" stroke="#ffd166" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="350" y="100" fill="#ffd166" font-family="Arial" font-size="14" font-weight="bold" transform="rotate(22, 350, 100)">Angled Plane (~75°)</text>

  <!-- Extruded Letters UTKARSHA along the angled plane -->
  <!-- Renders slanted text with 3D offset extrusion of 10 mm -->
  <!-- Let's render letter by letter or as a styled isometric group -->
  <g transform="matrix(0.9, 0.4, -0.15, 0.9, 570, 230)">
    <!-- 3D extrusion side walls (simulated by drawing offset steps) -->
    <text x="-150" y="-40" fill="#132b3f" font-family="Impact, Arial Black, Arial" font-size="78" font-weight="bold" letter-spacing="8" transform="skewX(-15)">UTKARSHA</text>
    <text x="-148" y="-39" fill="#132b3f" font-family="Impact, Arial Black, Arial" font-size="78" font-weight="bold" letter-spacing="8" transform="skewX(-15)">UTKARSHA</text>
    <text x="-146" y="-38" fill="#10253a" font-family="Impact, Arial Black, Arial" font-size="78" font-weight="bold" letter-spacing="8" transform="skewX(-15)">UTKARSHA</text>
    <!-- Top Face of Letters -->
    <text x="-145" y="-40" fill="#20d6b5" font-family="Impact, Arial Black, Arial" font-size="78" font-weight="bold" letter-spacing="8" stroke="#4da3ff" stroke-width="2.5" transform="skewX(-15)">UTKARSHA</text>
  </g>

  <!-- Extrusion dimension label -->
  <g fill="#20d6b5" font-family="Arial" font-size="15" font-weight="bold">
    <path d="M 680 150 L 710 135" stroke="#20d6b5" stroke-width="2"/>
    <path d="M 700 135 L 710 135 L 705 145" fill="#20d6b5"/>
    <text x="725" y="132">Extrude: 10 mm</text>
  </g>

  <!-- Letter height label -->
  <g fill="#ffd166" font-family="Arial" font-size="14" font-weight="bold">
    <line x1="330" y1="260" x2="385" y2="135" stroke="#ffd166" stroke-width="1.5"/>
    <line x1="325" y1="262" x2="335" y2="258" stroke="#ffd166" stroke-width="1.5"/>
    <line x1="380" y1="137" x2="390" y2="133" stroke="#ffd166" stroke-width="1.5"/>
    <text x="270" y="210">Height: 28 mm</text>
  </g>

  <polygon points="541.5,153.75 853.3,303.75 658.46,446.25 346.7,266.25" fill="none" stroke="#4da3ff" stroke-width="2.5"/>

  <rect x="250" y="550" width="700" height="40" fill="rgba(32, 214, 181, 0.08)" rx="6" stroke="rgba(32, 214, 181, 0.2)" stroke-width="1"/>
  <text x="600" y="575" text-anchor="middle" fill="#20d6b5" font-family="Arial" font-size="16" font-weight="bold">CAD Workflow: Angled construction plane → Sketch text "UTKARSHA" → Extrude Join to support legs</text>
</svg>"""

with open(os.path.join(image_dir, "phone_stand_step2.svg"), "w", encoding="utf-8") as f:
    f.write(step2_svg)

with open(os.path.join(image_dir, "phone_stand_step3.svg"), "w", encoding="utf-8") as f:
    f.write(step3_svg)

with open(os.path.join(image_dir, "phone_stand_step4.svg"), "w", encoding="utf-8") as f:
    f.write(step4_svg)

with open(os.path.join(image_dir, "phone_stand_step5.svg"), "w", encoding="utf-8") as f:
    f.write(step5_svg)

print("SVG files generated successfully!")
