# clap.py: double clap to control Spotify

import sys
import numpy as np
import sys
import time
from subprocess import Popen

block_size = 1024
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
		Popen(['spotify-dbus', 'PlayPause'])
		consec_claps = 0
	else:
		print "clap"

while True:
	block = np.fromfile(sys.stdin, dtype=np.int16, count=block_size)
	vol = np.mean( np.square(np.float32(block)) )
	if vol > clap_threshold:
		if debounce == 0:
			clap_event()
			debounce = 1
	else:
		debounce = 0