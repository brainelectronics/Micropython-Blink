# Micropython ESP32 Blink

Bare minimum Micropython Blink on an ESP32 or ESP8266


---------------


## Setup

The [esptool][ref-esptool] is required to flash the micropython firmware onto
the device.

For interaction with the filesystem of the device the
[Remote MicroPython shell][ref-remote-upy-shell] can be used.

### Installation

Install both python packages with the following command in a virtual
environment to avoid any conflicts with other packages installed on your local
system.

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Test both tools by showing their man/help info description.

```bash
esptool.py --help
rshell --help
```

### Flash firmware

To flash the [micropython firmware][ref-upy-firmware-download] as described on
the micropython firmware download page, use the `esptool.py` to erase the
flash before flashing the firmware.

```bash
esptool.py --chip esp32 --port /dev/tty.wchusbserial1410 erase_flash
esptool.py --chip esp32 --port /dev/tty.wchusbserial1410 --baud 460800 write_flash -z 0x1000 esp32-20210623-v1.16.bin
```

If the Micropython board is equipped with an external PSRAM chip, the
`esp32spiram-20210623-v1.16.bin` can also be used for ESP32 devices. If there
is no external PRSAM only the non SPIRAM version is working.

### Upload files to board

Download the `boot.py` and `main.py` file to the device using
[Remote MicroPython shell][ref-remote-upy-shell].

`boot.py` is similar to the `setup()` function in Arduino, the `main.py` is
equivalent to `loop()`.

Open the remote shell with the following command. Additionally use `-b 115200`
in case no CP210x is used but a CH34x to set the baudrate to 115200.

```bash
rshell -p /dev/tty.wchusbserial1410
```

Execute the folling commands inside the rshell to copy the files to the board.

```bash
# inside the rshell
cp blink.py /pyboard
cp boot.py /pyboard
cp main.py /pyboard
```

### Precompile module

The MicroPython board has to convert the provided `*.py` files during runtime
into a file that can be executed by the controller. To speed things up and to
reduce the CPU load these files can be cross-compiled on a computer and then
transfered to the MicroPython board.

See [MicroPython cross-compile README][ref-upy-cross-compile-readme]

> This will create a file foo.mpy which can then be copied to a place
> accessible by the target MicroPython runtime (eg onto a pyboard's
> filesystem), and then imported like any other Python module using import foo.

In this example the [`blink.py`][blink.py] file gets cross-compiled

```bash
python -m mpy_cross blink.py
rshell -p /dev/tty.wchusbserial1410
```

Execute the folling commands inside the rshell to copy the cross-compiled
file to the board and remove the prevoiusly copied, non cross-compiled file.

```bash
# inside the rshell
cp blink.mpy /pyboard
rm /pyboard/blink.py
```

<!-- Links -->
[ref-esptool]: https://github.com/espressif/esptool
[ref-remote-upy-shell]: https://github.com/dhylands/rshell
[ref-upy-firmware-download]: https://micropython.org/download/
[ref-upy-cross-compile-readme]: https://github.com/micropython/micropython/tree/master/mpy-cross
