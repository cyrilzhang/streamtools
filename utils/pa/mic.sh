#!/bin/bash

# pa/mic.sh: pipe mic output to stdout

DEVICE=alsa_input.pci-0000_00_1b.0.analog-stereo

if [ $# -ne 0 ]; then
	DEVICE=$1
fi

pacat --record --channels=1 --channel-map=mono --latency-msec=1 --device=$DEVICE
