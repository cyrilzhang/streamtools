# fft.py: pitch demo

import sys
import numpy as np
import time
import math
from subprocess import Popen
from scipy.fftpack import fft

sys.path = ['..'] + sys.path
from streamtools import *

stream = Stream()

while True:
	spec = stream.read_spec()
	print stream.sketch( spec )
	# classify(spec)