#!/bin/bash

# monitor.sh: pipe speaker output to stdout
if [ $# -ne 0 ]
	then
		pacat -r --latency-msec=1 -d $1
	else
		pacat -r --latency-msec=1 -d\
		alsa_output.usb-Logitech_Logitech_Z305-00-Z305.analog-stereo.monitor
fi