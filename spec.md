# Student Robotics KCH Specification
A Raspberry Pi 4 add-on board to protect and power the Pi from the v4 SR kit, and provide a visual indicator of the state of the brain board's software. Where appropriate the specification points from https://github.com/raspberrypi/hats are included inline.

## General
1. The board shall follow the naming convention of the other Student Robotics boards and be referred to as “Student Robotics KCH v1 Rev A” or shortened to SR KCHv1A.
2. All the board designs shall be open source.
3. All design work shall be completed in freely available software.
4. All design work should be completed in open source software.
5. The cost of each fully assembled board, along with case, should cost less than £16 including any development overhead.
6. The board shall have a location to write/label the asset code in human and machine readable forms, this should be visible without removing it from the Raspberry Pi.
7. The board should provide suitable test points and hardware to test the safety aspects of the board.
8. The board should be compatible with Raspberry Pi versions 3B+ and 4B.
9. The board should be labelled with an URL or QR Code to documentation.

## Mechanical
1. The board shall attach to the 40 pin header on the Raspberry Pi.
2. The board shall be compliant to the mechanical specifications for a Raspberry Pi HAT
3. The board shall use the mounting holes on the Raspberry Pi to provide mechanical strength to the Hat.
4. The board should be designed for single sided assembly, excluding the connectors.
5. The board and Raspberry Pi assembly shall be designed to fit inside a case (either an off-the-shelf case or one designed for it), with all connectors accessible.
6. The board may have a cutout to improve airflow over the Raspberry Pi’s CPU.

## Serial Connection
1. The board should provide a method to connect to the Raspberry Pi’s serial console.
2. The board may provide a USB to serial converter to connect to the Raspberry Pi’s serial console.

## GPIO
1. The board shall use the full 40 pin header.
2. The board shall stop external connections to the Raspberry Pi’s GPIO header.

## Power
1. The board shall use a Camdenboss CTB9550/2 7.5mm, or compatible connector, as the input power connection.
2. The board should accept an input voltage range of at least 7 volts to 15 volts.
3. The board shall provide the Raspberry Pi with a voltage of 5V (+/- 5%) across the full range of load.
4. The board shall provide a minimum output current of 3 amps.
5. The board shall provide reverse polarity protection and will not be damaged by connecting the input power backwards for an unlimited amount of time, including the low-side terminal being driven to a voltage other than USB ground.
6. The board should provide suitable transient input protection (ESD/TVS diodes).
7. The board shall support the Raspberry Pi being powered from the onboard USB-C power port on the Raspberry Pi, Powered from the Camcon on the Hat or both being provided at the same time without any piece of hardware being damaged.

## EEPROM
1. The board shall have an EEPROM containing the board information as defined in https://github.com/raspberrypi/hats.
2. The EEPROM shall be programmable with the board’s asset code so that it can be read back by the Raspberry Pi.
3. The EEPROM should have a hardware write-protect jumper to prevent accidental reprogramming from the Pi.

## User Interface
1. The board shall have an LED to indicate that power is connected.
2. The board should have an LED to indicate that the reverse polarity protection has been activated.
3. The board shall contain LEDs to indicate the stages of the boot process.
4. The board shall contain user controllable LEDs.
5. The user controllable LEDs should be RGB.
6. All LEDs shall have clear indications on the silkscreen of what they are.
7. Silkscreen markings for the LEDs should not be over specific to support future versions of Raspberry Pi software.

## Additional Notes
- A 5% tolerance on the 5V is a combination of the MXL7704 power management IC used, setting an under-voltage of 4.63V and the need to provide appropriate voltages to downstream USB devices which requires a voltage of 4.7V to 5.25V.

## Version History
- v1.0 Agreed 29.03.2022 in Kit Team Meeting
