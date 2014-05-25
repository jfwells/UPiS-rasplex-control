#!/usr/bin/python

#
#	Shut down for charging
#

import serial
import time
import os

ser = serial.Serial()
ser.baudrate = 38400
ser.port = "/dev/ttyAMA0"
ser.timeout = 1
ser.writeTimeout = 1

ser.open()
ser.write("@CHGR ON\r\n")
time.sleep(1)
ser.close()
