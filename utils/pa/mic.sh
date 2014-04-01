#!/bin/bash

# pa/mic.sh: pipe mic output to stdout
if [ $# -ne 0 ]
	then
		pacat -r --latency-msec=1 -d $1
	else
		pacat -r --latency-msec=1 -d\
		alsa_input.pci-0000_00_1b.0.analog-stereo
fi
