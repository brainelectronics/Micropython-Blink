# Micropython ESP32 Blink

Bare minimum Micropython Blink on an ESP32 or ESP8266


---------------


## Setup

The [esptool](https://github.com/espressif/esptool) is required to flash the
micropython firmware onto the device.

For interaction with the filesystem of the device the
[adafruit ampy package](https://github.com/scientifichackers/ampy) can be used.

### Installation

Install both python packages with the following command in a virtual
environment to avoid any conflicts with other packages installed on your local
system.

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install esptool
pip install adafruit-ampy
```

Test both tools by showing their man/help info description.

```bash
esptool.py --help
ampy --help
```

### Flash firmware

To flash the [micropython firmware](https://micropython.org/download/) as
described on the micropython firmware download page, use the `esptool.py` to
erase the flash before flashing the firmware.

```bash
esptool.py --chip esp32 --port /dev/tty.wchusbserial1410 erase_flash
esptool.py --chip esp32 --port /dev/tty.wchusbserial1410 --baud 460800 write_flash -z 0x1000 ../esp32-20210623-v1.16.bin
```

If the Micropython board is equipped with an external PSRAM chip, the
`esp32spiram-20210623-v1.16.bin` can also be used for ESP32 devices. If there
is no external PRSAM only the non SPIRAM version is working.

### Upload files to board

Download the `boot.py` and `main.py` file to the device. `boot.py` is similar
to the `setup()` function in Arduino, the `main.py` is equivalent to `loop()`.

```bash
# optional, show files existing on the device
ampy --port /dev/cu.wchusbserial1410 --baud 115200 ls -lr

# upload boot and main python file to the device
ampy --port /dev/cu.wchusbserial1410 --baud 115200 put boot.py
ampy --port /dev/cu.wchusbserial1410 --baud 115200 put main.py
```
