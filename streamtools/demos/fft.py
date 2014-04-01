# fft.py: sketch spectrum

import sys
import numpy as np
import time
import math
from scipy.fftpack import fft
from streamtools import *

stream = InStream()
while True:
	spec = stream.read_spec()
	print sketch(stream, spec)