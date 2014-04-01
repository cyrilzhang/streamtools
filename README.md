Cyril's Stream Tools
====================

Overview
--------

This is a wrapper for raw PCM audio streams, piped through stdin/stdout.
It lets you manipulate audio data as numpy arrays,
You'll need something that can pipe microphone input/speaker output
to binary streams, like PulseAudio's `pacat` or SoX.

Format for now is 16 bit stereo. Default sample rate is 44100 Hz.

Sample interaction (Ubuntu):

`utils/pa/mic.sh | utils/demo.sh fft`

C/C++ Utilities
---------------

`sconv`: converts 16-bit binary stereo stream to newline-separated decimal ints

Python Demos
------------

`clap.py`: run a script on double clap

`fft.py`: prints a sketchy live spectrogram

`learn.py`: cluster and classify sounds

`plot.py`: plot some spectra

`speedtest.py`: measures FFT performance
