#!/usr/bin/python

#
#	Get power status from UPiS from Rasplex
#	John Wells, 2014
#	Licence: GPL v3
#

import serial
import time
import os

ser = serial.Serial()
ser.baudrate = 38400
ser.port = "/dev/ttyAMA0"
ser.timeout = 1
ser.writeTimeout = 1


# Disable any pending timeouts
ser.open()
ser.write("@STOP\r\n")
time.sleep(1)
ser.close()

battery_power = ['BAT', 'LPR']

while True:
	ser.open()
	ser.write("@PM\r\n")
	upis_status = ser.read(25)
	ser.close()
	if any(s in upis_status for s in battery_power):
		print "on battery"

		ser.open()
		ser.write("@SDWN\r\n")
		time.sleep(1)
		response = ser.read(30)
		print "Sent shutdown"
		print response
		ser.close()
		time.sleep(5)
		os.system("/storage/upis/shutdown.sh")
		break
	else:
		print "Mains power"
	
	time.sleep(3)
