Cyril's Stream Tools
====================

Overview
--------

These tools take raw PCM data from stdin, and do fun stuff with it.
Requires numpy.

Format: 16 bit stereo, 44100 Hz

Works with PulseAudio (comes with Ubuntu) or SoX (`brew install sox`).

C/C++ Utilities
---------------

`sconv`: converts 16-bit binary stereo stream to newline-separated decimal ints

Python Demos
------------

`fft.py`: prints a sketchy live spectrogram

`speedtest.py`: measures FFT performance

`learn.py`: cluster and classify sounds

`clap.py`: run a script on double clap

Scripts
-------

`utils/pastream.sh`: PulseAudio stream

`utils/soxstream.sh`: SoX stream

`utils/stream.sh`: pick based on availability

`demos/demo.sh`: run demo; usage: `./demo.sh fft`

