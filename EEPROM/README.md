# Utilities to create, flash and dump HAT EEPROM images.

Original source of the scripts and templates:
https://github.com/raspberrypi/hats/tree/master/eepromutils

There is a complete, worked example at:
https://www.raspberrypi.org/forums/viewtopic.php?t=108134

## Usage
### On the Raspberry Pi

1. Add the following line to the `/boot/config.txt` file
```
dtparam=i2c_vc=on
```

2. Create tools with
```
make
```

3. Disable EEPROM write protection by shorting the two pins on the board

4. Make the device tree file
```
sudo dtc -@ -I dts -O dtb -o heartbeat.dtb heartbeat.dts
sudo chown pi:pi heartbeat.dtb
```

5. Make a file called `serial.txt` that contains only the serial number (no newline at the end)

6. Make the binary blob to go in the EEPROM
```
./eepmake eeprom_settings.txt hat.eep heartbeat.dtb -c serial.txt
```

6. Flash the blob to the EERPOM
```
sudo ./eepflash.sh -y -w -f=hat.eep -t=24c32
```

## Clearing the EEPROM
If things go bad this can be used to clear the contents of the EEPROM.
Resize as appropriate.
```
dd if=/dev/zero ibs=1k count=4 of=blank.eep
sudo ./eepflash.sh -w -f=blank.eep -t=24c32
```