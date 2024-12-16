import numpy as np
import matplotlib.pyplot as plt

sample_rate = 1000 
T = 1.0 / sample_rate 
t = np.arange(0, 1.0, T) 


freq1 = 5 
freq2 = 50  
signal = 0.5 * np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sign(np.sin(2 * np.pi * freq2 * t))


fft_result = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(len(fft_result), T)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Time Domain Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(fft_freq[:len(fft_freq)//2], np.abs(fft_result)[:len(fft_result)//2]) 
plt.title('Frequency Domain (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()

plt.tight_layout()
plt.show()
