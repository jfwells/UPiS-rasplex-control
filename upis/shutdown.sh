#!/bin/bash
#
#	Safe shutdown for Rasplex
#

LOCKDIR="/var/lock/"
LOCKFILE="xbmc.disabled"
LOGFILE="/storage/.upis_shutdown"

add_omit_pids() {
	omit_pids="$omit_pids -o $1"
}

date > $LOGFILE
touch "$LOCKDIR/$LOCKFILE"

echo 0x0 > /sys/devices/platform/bcm2708_usb/buspower

add_omit_pids $(pidof connmand)
add_omit_pids $(pidof dbus-daemon)
killall5 -15 $omit_pids
for seq in `seq 1 10` ; do
	usleep 500000
	clear > /dev/tty1
	killall5 -18 $omit_pids || break
done
sync
umount -a >/dev/null 2>&1
poweroff -f


