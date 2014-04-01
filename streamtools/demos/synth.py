# synth.py: output demo

import math
import numpy as np
from streamtools import *

out = OutStream()

s = 5
x = np.linspace(0,s*1,s*44100)
y = 400 * np.sin(x * 2*np.pi * 880 + 20*np.sin(x * 2*np.pi) )

out.write_block(y)
