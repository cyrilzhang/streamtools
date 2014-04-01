# output.py: speaker output

import sys
import numpy as np

class OutStream:
	# constructor
	def __init__(self, fd=sys.stdout, sample_rate=44100, block_size=4096):
		self.sample_rate = sample_rate
		self.block_size = block_size
		self.fd = fd

	# export binary contents
	def write_block(self, block):
		block.astype(np.int16).tofile(self.fd)