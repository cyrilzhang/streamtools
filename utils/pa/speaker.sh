#!/bin/bash

# speakers.sh: pipe stdin to speaker output
if [ $# -ne 0 ]
	then
		pacat --latency-msec=1 -d $1
	else
		pacat --latency-msec=1 -d\
		alsa_output.usb-Logitech_Logitech_Z305-00-Z305.analog-stereo
fi