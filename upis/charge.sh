#!/bin/bash

#kill $(pidof monitor.py)
echo 0x0 > /sys/devices/platform/bcm2708_usb/buspower
tvservice -o
PYTHONPATH=/storage/upis/lib /storage/upis/charge.py
shutdown.sh
