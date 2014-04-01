# utils.py: utility functions

import numpy as np
import math

# seconds to blocks
def seconds_to_blocks(stream, secs):
	return int(math.ceil( float(secs) * stream.sample_rate / stream.block_size ))

# hertz to index in fft
def hz_to_fft(stream, hz):
	return np.clip( int(float(hz) * stream.block_size / stream.sample_rate), 0, stream.block_size )

# index in fft to hertz
def fft_to_hz(stream, ind):
	return float(ind) * stream.sample_rate / stream.block_size

# sketchy ASCII art depiction of fft
def sketch(stream, spec, scale=1.0/8000, minfreq=200, maxfreq=2000, width=80):
	ret = ''
	asc = " `.~:<=tIYAXWH#M"
	for f in np.logspace(np.log10(minfreq), np.log10(maxfreq), num=width):
		ind = min(len(asc)-1, int(spec[ hz_to_fft(stream, f) ]*scale))
		ret += asc[ind]
	return ret
