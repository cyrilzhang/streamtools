#!/bin/bash
rec -r 44100 -c 2 /dev/dsp -sLb 16 -t raw - # 2>/dev/null
