# learn.py: classify claps/snaps/voice

import sys
import numpy as np
import time
import math

from scipy.fftpack import fft
from scipy.signal import medfilt
from scipy.linalg import norm

sys.path = ['..'] + sys.path
from streamtools import *

silence = np.load("data/silence.npy")

# wait for an event to finish
def record_event(stream, threshold=200000):
	frame = 0
	avg = np.zeros(4096)
	while True:
		spec = medfilt( stream.read_spec() ) - silence
		n = norm( spec )
		if n > threshold:
			if frame == 0:
				print "begin event"
			frame += 1
			# print "event: frame=%d, norm=%f" % (frame, n)
			avg += spec
		else:
			if frame > 0:
				# print "end event"
				break
	return avg / frame

def learn_silence(filename, secs=20):
	print "recording; shut up!"
	stream = Stream()
	nblocks = stream.seconds(secs)
	blocks = np.zeros((nblocks, 4096))
	for i in range(nblocks):
		spec = medfilt( stream.read_spec() )
		blocks[i,:] = spec
		print "norm:", norm(spec)
	med = np.median(blocks, axis=0)
	print "silence learned:", filename
	np.save(filename, med)


# wait for n trials of an event
def learn(filename, tries=20):
	print "learning: ", filename
	tot = np.zeros(4096)
	stream = Stream()
	for i in range(tries):
		evt = record_event(stream)
		evt /= norm(evt)
		tot += evt
		print "recorded instance", i+1

	tot /= norm(tot)
	np.save("data/"+filename, tot)
	print "learned:", filename

# classify an event
def classify():
	# load data
	sound_names = ["clap", "snap", "voice"]
	sounds = np.zeros((len(sound_names), 4096))
	for i,sn in enumerate(sound_names):
		sounds[i,:] = np.load("data/"+sn+".npy")

	stream = Stream()
	while True:
		evt = record_event(stream)
		evt /= norm(evt)

		csv = np.dot(sounds, evt)
		print csv
		print stream.sketch(evt, scale=100)
		print stream.sketch(sounds[np.argmax(csv)], scale=100)
		print sound_names[np.argmax(csv)], "(%d%% sure)" % (np.max(csv)*100)

		for i in range(2):
			stream.read_block()

# learn_silence("data/silence.npy")
classify()