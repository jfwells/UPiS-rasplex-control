Detect UPiS UPS power status from Raspberry Pi running RasPlex
==============================================================

Simply copy the upis directory to the /storage  directory in RasPlex. This will survive across updates.

Then add the following to /storage/.config/autostart.sh:

(PYTHONPATH=/storage/upis/lib /storage/upis/monitor.py;) &


Notes
-----

1. Includes [PySerial](http://pyserial.sourceforge.net/), Copyright (C) 2001-2013 Chris Liechti <cliechti(at)gmx.net>, released under the Python license. As RasPlex doesn't have the ability to compile Python libries at run-time, the library is included statically in /lib, and can be run from source.
1. The Charge.sh script can be used for manually charging the UPiS if your power draw is too high to prevent charging during runtime. The script shuts down the Raspberry Pi but leaves the UPiS running. You can power cycle to return to normal.
