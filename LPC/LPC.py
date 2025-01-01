import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import lfilter

def lpc(signal, order):
    n = len(signal)
    r = np.correlate(signal, signal, mode='full')[n-1:]
    r = r[:order+1]

    R = np.zeros((order+1, order+1))
    for i in range(order+1):
        R[i, :order+1-i] = r[i:i+order+1-i]

    a = np.zeros(order+1)
    a[0] = 1.0
    e = r[0]

    for i in range(1, order+1):
        k = r[i]
        for j in range(1, i):
            k -= a[j] * r[i-j]
        k /= e
        a[i] = k
        for j in range(1, i):
            a[j] -= k * a[i-j]
        e *= (1 - k**2)

    return a

sample_rate, data = wavfile.read('./15-15- amozesh dadan.wav')

if data.ndim > 1:
    data = data[:, 0]

data = data / np.max(np.abs(data))

order = 12

lpc_coeffs = lpc(data, order)

print("LPC Coefficients:", lpc_coeffs)

excitation = np.random.randn(len(data))


synthesized_signal = lfilter([1], lpc_coeffs, excitation)

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(data)
plt.title('Original Signal')
plt.subplot(2, 1, 2)
plt.plot(synthesized_signal)
plt.title('Synthesized Signal from LPC')
plt.tight_layout()
plt.show()
