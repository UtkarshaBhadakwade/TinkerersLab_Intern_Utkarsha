"""Wire image folder assets into technical-innovation.html."""
from pathlib import Path

path = Path(r"C:\Users\hp\OneDrive\Desktop\TinkeresLab\technical-innovation.html")
content = path.read_text(encoding="utf-8")

# Global broken-path fixes
broken = {
    "image/WhatsApp Image 2026-06-10 at 8.17.53 PM.jpeg": "image/phone_stand_reference.svg",
    "image/Bambu-Lab-H2D-32415_3.jpg": "image/bambu_printer_reference.svg",
    "image/bambu_studio_interface.png": "image/bambu_printer_reference.svg",
    "image/3D-Printed-Boat.png": "image/bambu_printer_reference.svg",
    "image/IPR-India.jpg": "image/ipr-session-poster.jpeg",
}
for old, new in broken.items():
    content = content.replace(old, new)

# Context-specific src replacements (old src + alt fragment -> new src)
alt_replacements = [
    ("image/arduino_ide_reference.svg", "Arduino IDE download page reference", "image/arduino_ide_search.png"),
    ("image/arduino_ide_reference.svg", "Downloaded Arduino IDE installer reference", "image/downloading-and-installing-img01.png"),
    ("image/arduino_ide_reference.svg", "Arduino IDE main window reference", "image/arduino_ide_bareminimum_1.png"),
    ("image/arduino_ide_reference.svg", "Arduino IDE board and port selection reference", "image/arduino_ide_bareminimum_2.png"),
    ("image/arduino_ide_reference.svg", "Arduino IDE Blink example upload reference", "image/arduino_ide_done_uploading.png"),
    ("image/arduino_ide_reference.svg", "Arduino IDE cloud connectivity reference", "image/iot-cloud-data-flow-reference.svg"),
    ("image/sensor_actuator_reference.svg", "Common sensor examples including LDR, PIR, DHT11, and gas sensor", "image/electronic_sensors.png"),
    ("image/sensor_actuator_reference.svg", "Common actuator examples including motor, servo, relay, and buzzer", "image/electronic_actuators.png"),
    ("image/microcontroller_boards_reference.svg", "Reference comparison of common microcontroller boards", "image/microcontroller_vs_microprocessor.png"),
    ("image/arduino_uno_pinout.svg", "Arduino Uno board and pinout reference", "image/arduino_uno_board.svg"),
    ("image/arduino_nano_pinout.svg", "Arduino Nano board and pinout reference", "image/arduino_nano_board.svg"),
    ("image/arduino_mega_pinout.svg", "Arduino Mega board and pinout reference", "image/arduino_mega_board.svg"),
    ("image/esp32_pinout.svg", "ESP32 development board and pinout reference", "image/esp32_photo.png"),
    ("image/arduino_uno_pinout.svg", "Arduino Uno full board and pinout reference", "image/arduino_uno_complete_pinout.svg"),
    ("image/arduino_uno_pinout.svg", "Arduino Uno power pins reference", "image/arduino_uno_power_pins.svg"),
    ("image/arduino_uno_pinout.svg", "Arduino Uno digital pins with PWM, serial, and SPI labels", "image/arduino_uno_digital_pins.svg"),
    ("image/arduino_uno_pinout.svg", "Arduino Uno analog pins A0 to A5 reference", "image/arduino_uno_analog_pins.svg"),
    ("image/arduino_uno_pinout.svg", "Arduino Uno UART, I2C, SPI, and ICSP pin reference", "image/arduino_uno_comm_pins.svg"),
    ("image/arduino_uno_pinout.svg", "Complete Arduino Uno pinout diagram", "image/arduino_uno_complete_pinout.svg"),
    ("image/arduino_mega_pinout.svg", "Arduino Mega board reference", "image/arduino_mega_board.svg"),
    ("image/arduino_mega_pinout.svg", "Arduino Mega pinout diagram", "image/arduino_mega_pinout_diagram.svg"),
    ("image/arduino_mega_pinout.svg", "Arduino Mega with multiple component connection reference", "image/arduino-mega-multimodule-reference.svg"),
    ("image/arduino_nano_pinout.svg", "Arduino Nano board reference", "image/arduino_nano_board.svg"),
    ("image/arduino_nano_pinout.svg", "Arduino Nano pinout diagram", "image/arduino_nano_pinout_diagram.svg"),
    ("image/arduino_nano_pinout.svg", "Arduino Nano breadboard circuit reference", "image/arduino_nano_breadboard.svg"),
    ("image/esp32_pinout.svg", "ESP32 board and pinout reference", "image/esp32_pinout.svg"),
    ("image/esp32_pinout.svg", "ESP32 development board reference", "image/esp32_photo.png"),
    ("image/esp32_pinout.svg", "ESP32 pinout diagram", "image/esp32_pinout.svg"),
    ("image/arduino_nano_pinout.svg", "Arduino Nano IoT board and pin reference", "image/arduino_nano_board.svg"),
    ("image/esp32_pinout.svg", "ESP32 board and pinout reference", "image/iot-board-selection-reference.svg"),
    ("image/firebase_iot_reference.svg", "Firebase IoT dashboard reference", "image/firebase_overview.svg"),
    ("image/firebase_iot_reference.svg", "ESP32 Firebase connection reference", "image/firebase_board_connections.svg"),
    ("image/firebase_iot_reference.svg", "Sensor values stored in Firebase reference", "image/firebase_architecture.png"),
    ("image/firebase_code_reference.svg", "ESP32 Firebase Arduino IDE code structure reference", "image/firebase_code_structure.svg"),
]

for old_src, alt_fragment, new_src in alt_replacements:
    needle = f'src="{old_src}" class="project-image" alt="{alt_fragment}"'
    replacement = f'src="{new_src}" class="project-image" alt="{alt_fragment}"'
    if needle in content:
        content = content.replace(needle, replacement, 1)
    else:
        print("WARN: not found:", alt_fragment[:60])

# Update placeholder tags to match new src values
for old, new in broken.items():
    content = content.replace(f"Image File Reference: {old}", f"Image File Reference: {new}")

# Week 2 Day 1 laser section - add images
laser_intro = """                </ul>
            </div>
        </div>

        <div class="doc-box">"""
laser_intro_img = """                </ul>
            </div>
            <div class="image-placeholder-container">
                <span class="placeholder-tag">Image File Reference: image/user_laser_machine.jpg</span>
                <img src="image/user_laser_machine.jpg" class="project-image" alt="CO2 laser cutting machine in the Tinkerers Lab">
            </div>
        </div>

        <div class="doc-box">"""
content = content.replace(laser_intro, laser_intro_img, 1)

laser_components = """                    <li><strong>Motion and Control System:</strong> Stepper motors, belts, rails, controller board, and software move the cutting head accurately along the X and Y axes.</li>
                </ol>
            </div>
        </div>

        <h2 style="color: #00ffd5; margin-top: 50px;"""
laser_components_img = """                    <li><strong>Motion and Control System:</strong> Stepper motors, belts, rails, controller board, and software move the cutting head accurately along the X and Y axes.</li>
                </ol>
            </div>
            <div class="image-placeholder-container">
                <span class="placeholder-tag">Image File Reference: image/co2_laser_components.png</span>
                <img src="image/co2_laser_components.png" class="project-image" alt="Internal CO2 laser tube, mirrors, and cutting head components">
            </div>
        </div>

        <h2 style="color: #00ffd5; margin-top: 50px;"""
content = content.replace(laser_components, laser_components_img, 1)

laser_workflow = """                    <li>Start the chiller first, switch on exhaust ventilation, close the lid, and then run the laser job safely.</li>
                </ol>
            </div>
        </div>

        <div class="doc-box">
            <h2>Important Safety and Machine Care</h2>"""
laser_workflow_img = """                    <li>Start the chiller first, switch on exhaust ventilation, close the lid, and then run the laser job safely.</li>
                </ol>
            </div>
            <div class="image-placeholder-container">
                <span class="placeholder-tag">Image File Reference: image/laser_software_design.png</span>
                <img src="image/laser_software_design.png" class="project-image" alt="Vector design software layout prepared for laser cutting">
            </div>
        </div>

        <div class="doc-box">
            <h2>Important Safety and Machine Care</h2>"""
content = content.replace(laser_workflow, laser_workflow_img, 1)

laser_chart = """                    <li><strong>Thermocol Cutting:</strong> Needs careful control because it melts easily under heat.</li>
                </ul>
            </div>
        </div>

        <div class="doc-box">
            <h2>Laser Cutting Applications</h2>"""
laser_chart_img = """                    <li><strong>Thermocol Cutting:</strong> Needs careful control because it melts easily under heat.</li>
                </ul>
            </div>
            <div class="image-placeholder-container">
                <span class="placeholder-tag">Image File Reference: image/user_laser_chart.png</span>
                <img src="image/user_laser_chart.png" class="project-image" alt="Laser cutter speed, power, and mode reference chart">
            </div>
        </div>

        <div class="doc-box">
            <h2>Laser Cutting Applications</h2>"""
content = content.replace(laser_chart, laser_chart_img, 1)

laser_apps = """                <li>Preparing clean 2D parts for product design and fabrication projects</li>
            </ul>
        </div>
        </div>
    </div>

    <!-- WEEK 2 DAY 2 -->"""
laser_apps_img = """                <li>Preparing clean 2D parts for product design and fabrication projects</li>
            </ul>
            <div class="image-placeholder-container">
                <span class="placeholder-tag">Image File Reference: image/user_laser_cutting.png</span>
                <img src="image/user_laser_cutting.png" class="project-image" alt="Laser cutter in operation with cut shapes on the bed">
            </div>
        </div>
        </div>
    </div>

    <!-- WEEK 2 DAY 2 -->"""
content = content.replace(laser_apps, laser_apps_img, 1)

# Add has-img class to laser doc boxes
for marker in [
    '<div class="doc-box">\n            <h2>Introduction to Laser Cutting</h2>',
    '<div class="doc-box">\n            <h2>Three Main Components of the CO2 Laser Cutter</h2>',
    '<div class="doc-box">\n            <h2>Design to Cut Process</h2>',
    '<div class="doc-box">\n            <h2>Speed, Power, and Mode Settings</h2>',
    '<div class="doc-box">\n            <h2>Laser Cutting Applications</h2>',
]:
    content = content.replace(marker, marker.replace('doc-box', 'doc-box has-img', 1), 1)

# Fix missing ESP32 common uses image
missing_esp32 = """            <div class="image-placeholder-container">
                <span class="placeholder-tag">Image File Reference: image/firebase_iot_reference.svg</span>
                
            </div>
        </div>

        <div class="doc-box has-img">
            <h2>Physical ESP32 Board</h2>"""
fixed_esp32 = """            <div class="image-placeholder-container">
                <span class="placeholder-tag">Image File Reference: image/iot-dashboard-control-reference.svg</span>
                <img src="image/iot-dashboard-control-reference.svg" class="project-image" alt="IoT dashboard and ESP32 control reference">
            </div>
        </div>

        <div class="doc-box has-img">
            <h2>Physical ESP32 Board</h2>"""
content = content.replace(missing_esp32, fixed_esp32, 1)

# Arduino IDE step 3 - add install article image alongside linux download
install_block = """            <figure class="image-figure">
                <img src="image/arduino_ide_download_linux.png" class="project-image" alt="Arduino IDE Linux ARM 32 bits download link">
                <figcaption>Arduino IDE download options</figcaption>
            </figure>"""
install_block_new = """            <div class="image-placeholder-container">
                <span class="placeholder-tag">Image File Reference: image/arduino_ide_install_article.png</span>
                <img src="image/arduino_ide_install_article.png" class="project-image" alt="Official Arduino IDE download and installation guide">
            </div>
            <figure class="image-figure">
                <img src="image/arduino_ide_download_linux.png" class="project-image" alt="Arduino IDE Linux ARM 32 bits download link">
                <figcaption>Arduino IDE download options</figcaption>
            </figure>"""
content = content.replace(install_block, install_block_new, 1)

path.write_text(content, encoding="utf-8")
print("Updated", path)
