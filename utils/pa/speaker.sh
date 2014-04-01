#!/bin/bash

# speakers.sh: pipe stdin to speaker output
DEVICE=alsa_output.usb-Logitech_Logitech_Z305-00-Z305.analog-stereo

if [ $# -ne 0 ]; then
	DEVICE=$1
fi

pacat --channels=1 --channel-map=mono --latency-msec=1 --device=$DEVICE