import numpy as np
import matplotlib.pyplot as plt
import librosa


def cepstral_analysis(signal, sampling_rate, frame_size, overlap):
    step = frame_size - overlap
    num_frames = (len(signal) - overlap) // step
    frames = np.array([signal[i * step:i * step + frame_size] for i in range(num_frames)])
    
    cepstral_features = []
    
    for frame in frames:
        spectrum = np.fft.fft(frame)
        
        log_spectrum = np.log(np.abs(spectrum) + 1e-8)
        
        cepstrum = np.fft.ifft(log_spectrum)
        
        cepstral_features.append(np.real(cepstrum))
    
    return np.array(cepstral_features)


def analyze_audio(file_path):
    signal, sampling_rate = librosa.load(file_path, sr=16000)
    
    frame_size = 512
    overlap = 256

    cepstral_features = cepstral_analysis(signal, sampling_rate, frame_size, overlap)

    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    time = np.linspace(0, len(signal) / sampling_rate, len(signal))
    plt.plot(time, signal)
    plt.title("Original Audio Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    
    plt.subplot(2, 1, 2)
    plt.imshow(cepstral_features.T, aspect='auto', cmap='viridis', extent=[0, len(signal) / sampling_rate, 0, 256])
    plt.colorbar(label="Cepstral Coefficient Value")
    plt.title("Cepstral Coefficients")
    plt.xlabel("Time (s)")
    plt.ylabel("Cepstral Coefficient Index")
    
    plt.tight_layout()
    plt.show()

file_path = './15-15- amozesh dadan.wav'

analyze_audio(file_path)
