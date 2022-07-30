#! /bin/bash

while true; do
    echo -n "Asset code: "
    read SERIAL
    PS3="Flash asset code '$SERIAL' to EEPROM?"
    options=("Yes" "No")
    select opt in "${options[@]}"; do
        case $opt in
            "Yes") break;;
            "No") continue 2;;
            *) echo "invalid option $REPLY";;
        esac
    done

    # Bake in serial
    echo "$SERIAL" > serial.txt
    ./eepmake eeprom_settings.txt hat.eep heartbeat.dtb -c serial.txt
    echo -n "Press enter to flash EEPROM"
    read
    sudo ./eepflash.sh -y -w -f=hat.eep -t=24c32

    # Verify EEPROM
    sudo ./eepflash.sh -y -r -f=hat_verify.eep -t=24c32

    # truncate to same size
    sudo truncate -s $(cat hat.eep|wc -c) hat_verify.eep

    if ! diff -q hat.eep hat_verify.eep; then
        echo "EEPROM verification failed"
        continue
    fi

    # Test LEDs
    echo -n "Press enter to test LEDs"
    read
    python3 ../test/test_all_leds.py
done
