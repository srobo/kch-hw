# KCH - Raspberry Pi Hat

A Raspberry Pi 4 add-on board to protect and power the Pi from the v4 SR kit, and provide a visual indicator of the state of the brain board's software as detailed in the [specification](./spec.md).

## The UI
The UI is illustrated below.

![UI design](./kch_ui.svg)

## Manufacturing
The board was designed to be manufactured using [JLCPCB](https://jlcpcb.com/) for both the PCB and assembly. This is using as 2 layer board with single sided assembly. The two through-hole connectors are rear-mounted and manually added after.

The BOM and assembly files can be generated with [KiCAD JLCPCB tools](https://github.com/Bouni/kicad-jlcpcb-tools) and the JLCPCB part codes are already assigned.

## Pinout

Header Pin | GPIO | Function
--- | --- | ---
1   | - | -
2   | - | 5V
3   | - | -
4   | - | 5V
5   | - | -
6   | - | GND
7   | 4 | USER C Red LED
8   | 14| UART TX
9   | - | GND
10  | 15| UART RX
11  | 17| USER C Blue LED
12  | 18| USER C Green LED
13  | 27| USER B Red LED
14  | - | GND
15  | 22| USER B Blue LED
16  | 23| USER B Green LED
17  | - | 3.3V
18  | 24| USER A Red LED
19  | 10| USER A Green LED
20  | - | GND
21  | 9 | Start LED
22  | 25| USER A Blue LED
23  | 11| Code LED
24  | 8 | WiFi LED
25  | - | GND
26  | 7 | BOOT 20% LED
27  | 0 | EEPROM SDA
28  | 1 | EEPROM SCL
29  | 5 | BOOT 40% LED
30  | - | GND
31  | 6 | BOOT 80% LED
32  | 12| BOOT 60% LED
33  | 13| BOOT 100% LED
34  | - | GND
35  | 19| Heartbeat LED
36  | 16| Comp LED
37  | 26| Status Red LED
38  | 20| Status Green LED
39  | - | GND
40  | 21| Status Blue LED
