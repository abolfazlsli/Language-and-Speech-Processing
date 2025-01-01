import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def hps(signal, sample_rate, max_harmonics=5):
    spectrum = np.fft.fft(signal)
    spectrum_magnitude = np.abs(spectrum)[:len(spectrum) // 2]

    hps_result = spectrum_magnitude.copy()

    for h in range(2, max_harmonics + 1):
        downsampled_spectrum = np.zeros_like(spectrum_magnitude)
        downsampled_spectrum[:len(spectrum_magnitude) // h] = spectrum_magnitude[h-1::h]
        hps_result[:len(downsampled_spectrum)] *= downsampled_spectrum

    return hps_result

sample_rate, data = wavfile.read('./Mehrad Hidden - Rakab.wav')


if data.ndim > 1:
    data = data[:, 0]

data = data / np.max(np.abs(data))

hps_result = hps(data, sample_rate)

frequencies = np.fft.fftfreq(len(hps_result), 1/sample_rate)[:len(hps_result)]


plt.figure(figsize=(12, 6))
plt.plot(frequencies, hps_result)
plt.title('Harmonic Product Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, sample_rate / 2)
plt.grid()
plt.show()
