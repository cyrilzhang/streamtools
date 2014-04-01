# fft.py: sketch spectrum

import sys
import numpy as np
import time
import math
from scipy.fftpack import fft
from streamtools import *

stream = InStream()
for spec in iter(stream.read_spec, None):
	print sketch(stream, spec)