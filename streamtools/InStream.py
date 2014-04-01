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
		block = np.fromfile(self.fd, dtype=np.int16, count=self.block_size)
		if block.size != self.block_size:
			return None
		return block

	# magnitude of FFT
	def read_spec(self):
		block = self.read_block()
		if block == None:
			return None
		return np.absolute( scipy.fftpack.fft( block ) )
