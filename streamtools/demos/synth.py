# synth.py: output demo

import math
import numpy as np
from streamtools import *

out = OutStream()

x = np.linspace(0,1,44100)
y = 100 * np.sin(x * 2*math.pi * 880.0)

out.write_block(y)
