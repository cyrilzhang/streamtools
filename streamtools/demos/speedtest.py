# speedtest.py: FFT benchmark

import sys
import time
import math

import numpy as np
from scipy.fftpack import fft
from streamtools import *

def time_fft(secs=10):
	print "Capturing for", secs, "seconds"
	stream = InStream()
	nblocks = seconds_to_blocks(stream, secs)

	avg_read = 0 # should be 44100 Hz
	avg_fft = 0 # should be faster than 44100 Hz

	for i in range(nblocks):
		read_begin = time.time()
		block = stream.read_block()
		fft_begin = time.time()
		spec = np.absolute( fft(block) )
		end = time.time()
		avg_read += end - read_begin
		avg_fft += end - fft_begin

	avg_read /= nblocks
	avg_fft /= nblocks

	avg_read = stream.block_size / avg_read
	avg_fft = stream.block_size / avg_fft

	print "Read: %.1lf Hz" % avg_read
	print "FFT: %.1lf Hz" % avg_fft

time_fft(30)