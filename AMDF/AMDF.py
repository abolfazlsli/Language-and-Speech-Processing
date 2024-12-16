import numpy as np
import librosa
import matplotlib.pyplot as plt


def calculate_amdf(signal, max_lag):
    N = len(signal)
    amdf = np.zeros(max_lag)
    
    for tau in range(1, max_lag):
        amdf[tau] = np.sum(np.abs(signal[:N - tau] - signal[tau:N]))
    
    return amdf

def analyze_audio(file_path):
    signal, sampling_rate = librosa.load(file_path, sr=16000)

    signal = signal[:2000]
    max_lag = 100

    amdf_values = calculate_amdf(signal, max_lag)

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    time_axis = np.linspace(0, len(signal) / 16000, len(signal))
    plt.plot(time_axis, signal)
    plt.title("Original Audio Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.subplot(2, 1, 2)
    plt.plot(range(1, max_lag), amdf_values[1:])
    plt.title("AMDF - Average Magnitude Difference Function")
    plt.xlabel("Lag (samples)")
    plt.ylabel("AMDF Value")
    
    plt.tight_layout()
    plt.show()


file_path = './15-15- amozesh dadan.wav'

analyze_audio(file_path)
