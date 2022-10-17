import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.plot(3)
fs = 1000

t = np.linspace(0,10,10*fs)
y = 3+2*np.sin(2*np.pi*200*t) - 4*np.cos(2*np.pi*500*t)

spec = np.fft.fft(y)

N = len(spec)

spec = spec/N
spec_pos = spec[0:N//2]
freqs = (fs/N)*np.arange(0,N/2)
plt.plot(N,spec)
plt.show()


