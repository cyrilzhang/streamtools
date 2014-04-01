# clap.py: double clap to execute an arbitrary shell script

import sys
import numpy as np
import sys
import time
from subprocess import Popen

import streamtools as st

clap_threshold = 1e6
debounce = 0

last_clap = 0
consec_claps = 0

def clap_event():
	global last_clap, consec_claps

	clap_time = time.clock()
	clap_dur = clap_time - last_clap
	last_clap = clap_time

	if clap_dur < 1:
		consec_claps += 1
	else:
		consec_claps = 1

	if consec_claps == 2:
		print "dblclap"
		Popen(sys.argv[1:])
		consec_claps = 0
	else:
		print "clap"

stream = InStream(block_size=1024)

while True:
	block = stream.read_block()
	vol = np.mean( np.square(np.float32(block)) )
	if vol > clap_threshold:
		if debounce == 0:
			clap_event()
			debounce = 1
	else:
		debounce = 0