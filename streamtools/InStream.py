# input.py: mic input

import sys
import numpy as np
import math
import scipy.fftpack

class InStream:
	# constructor
	def __init__(self, fd=sys.stdin, sample_rate=44100, block_size=4096):
		self.sample_rate = sample_rate
		self.block_size = block_size
		self.fd = fd

	# read mono channel
	def read_block(self):
		return np.fromfile(self.fd, dtype=np.int16,count=self.block_size)

	# magnitude of FFT
	def read_spec(self):
		return np.absolute( scipy.fftpack.fft( self.read_block() ) )
