# pitch.py: classify pitch

import sys
import numpy as np
import time
import math
from scipy.fftpack import fft
from streamtools import *

run = []

# classify notes
def classify(spec):
	global run, stream

	q = np.argmax(spec[20:len(spec)/3])+20
	if spec[q] > 100000:
		center = np.average(np.array(range(q-3,q+4)), weights=spec[q-3:q+4])
		hz = fft_to_hz(stream, center)
		note = np.fmod(12 * np.log(hz/440)/np.log(2), 12)
		# print 12 * np.fmod( np.log(hz/440)/np.log(2), 1 )
		run.append( note )
	else:
		if len(run) > 4:
			r = np.array(run[2:-1])
			base = r[0]
			r -= base
			note = base + r.mean()
			cents = (np.fmod(note+100.5,1)-0.5) * 100
			print "%s %0d" % (['A', 'A#', 'B', 'C', 'C#', 'D', 'D#',
				'E', 'F', 'F#', 'G', 'G#', 'A'][int(np.round(note))], cents)
		run = []

stream = InStream()
while True:
	spec = stream.read_spec()
	classify(spec)