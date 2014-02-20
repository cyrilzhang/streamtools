# streamtools.py: stream tools library

import sys
import numpy as np
import math
import sys
import scipy.fftpack

##### STREAM CLASS #####

class Stream:
	def __init__(self, sample_rate_=44100, block_size_=4096):
		self.sample_rate = sample_rate_
		self.block_size = block_size_
		self.blocks_per_second = float(sample_rate_)/block_size_

	def read_block(self): # read mono channel
		block = np.fromfile(sys.stdin, dtype=np.int16,count=2*self.block_size)\
			.reshape(2,self.block_size)
		return block[0] + block[1]

	def read_spec(self): # magnitude of FFT
		return np.absolute( scipy.fftpack.fft( self.read_block() ) )

	def seconds(self, secs): # seconds to blocks
		return int(math.ceil( secs * self.blocks_per_second ))

	def hz_to_fft(self, hz): # hertz to index in fft
		return np.clip( int(hz / self.blocks_per_second), 0, self.block_size )

	def fft_to_hz(self, ind): # index in fft to hertz
		return float(ind) * self.blocks_per_second

	def sketch(self, spec, scale=1.0/8000, minfreq=200, maxfreq=2000, width=80):
		ret = ''
		asc = " `.~:<=tIYAXWH#M"
		for f in np.logspace(np.log10(minfreq), np.log10(maxfreq), num=width):
			ind = min(len(asc)-1, int(spec[ self.hz_to_fft(f) ]*scale))
			ret += asc[ind]
		return ret
