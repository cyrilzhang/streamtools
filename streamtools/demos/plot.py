# plot.py: plot spectra

import sys
import numpy as np
import time
import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft

import streamtools as st

stream = st.InStream(block_size=8192)

plt.clf()
plt.yscale('log')

N = 50
specs = np.zeros((N,stream.block_size))

for i in range(N):
	specs[i,:] = stream.read_spec()

avg = np.mean(specs, axis=0)
med = np.median(specs, axis=0)
std = np.std(specs, axis=0)

plt.plot(avg, color='red')
plt.plot(med, color='blue')
plt.plot(avg+std, color='pink')
plt.plot(avg-std, color='pink')

plt.show()