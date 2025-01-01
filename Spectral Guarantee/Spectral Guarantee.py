import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

sample_rate, data = wavfile.read('./Mehrad Hidden - Rakab.wav')

spectrum = np.fft.fft(data)
frequency = np.fft.fftfreq(len(spectrum), 1/sample_rate)


spectrum = np.where(spectrum < 0, 0, spectrum)

plt.figure(figsize=(12, 6))
plt.plot(frequency, np.abs(spectrum))
plt.title('Spectral Guarantee')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, sample_rate / 2)
plt.grid()
plt.show()
