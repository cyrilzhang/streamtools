# input.py: mic input

import sys
import numpy as np
import math
import scipy.fftpack

class InStream:
	# constructor
	def __init__(self, source=sys.stdin, sample_rate=44100, block_size=4096):
		self.sample_rate = sample_rate
		self.block_size = block_size
		self.blocks_per_second = float(sample_rate)/block_size
		self.source = source

	# read mono channel
	def read_block(self):
		block = np.fromfile(self.source, dtype=np.int16,count=2*self.block_size)\
			.reshape(2,self.block_size)
		return block[0] + block[1]

	# magnitude of FFT
	def read_spec(self):
		return np.absolute( scipy.fftpack.fft( self.read_block() ) )

	# seconds to blocks
	def seconds(self, secs):
		return int(math.ceil( secs * self.blocks_per_second ))

	# hertz to index in fft
	def hz_to_fft(self, hz):
		return np.clip( int(hz / self.blocks_per_second), 0, self.block_size )

	# index in fft to hertz
	def fft_to_hz(self, ind):
		return float(ind) * self.blocks_per_second

	# sketchy ASCII art depiction of fft
	def sketch(self, spec, scale=1.0/8000, minfreq=200, maxfreq=2000, width=80):
		ret = ''
		asc = " `.~:<=tIYAXWH#M"
		for f in np.logspace(np.log10(minfreq), np.log10(maxfreq), num=width):
			ind = min(len(asc)-1, int(spec[ self.hz_to_fft(f) ]*scale))
			ret += asc[ind]
		return ret
