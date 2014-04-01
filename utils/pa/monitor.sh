#!/bin/bash

# monitor.sh: pipe speaker output to stdout

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
exec $DIR/mic.sh alsa_output.usb-Logitech_Logitech_Z305-00-Z305.analog-stereo.monitor
