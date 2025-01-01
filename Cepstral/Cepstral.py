import numpy as np
import matplotlib.pyplot as plt


def cepstral_analysis(signal, frame_size, overlap, sampling_rate):
    step = frame_size - overlap
    num_frames = (len(signal) - overlap) // step
    frames = np.array([signal[i*step:i*step+frame_size] for i in range(num_frames)])
    
    cepstral_coeffs = []
    for frame in frames:
        spectrum = np.fft.fft(frame)
        log_spectrum = np.log(np.abs(spectrum) + 1e-8)
        cepstrum = np.fft.ifft(log_spectrum)
        cepstral_coeffs.append(np.real(cepstrum))
    
    return np.array(cepstral_coeffs)



def create_signal():
    sampling_rate = 1000
    t = np.linspace(0, 1, sampling_rate)
    signal = np.sin(2 * np.pi * 100 * t) + 0.5 * np.sin(2 * np.pi * 200 * t)
    return signal, sampling_rate


def main():
    signal, sampling_rate = create_signal()
    
    frame_size = 256
    overlap = 128

    cepstral_features = cepstral_analysis(signal, frame_size, overlap, sampling_rate)

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(signal)
    plt.title("Signal")
    
    plt.subplot(2, 1, 2)
    plt.imshow(cepstral_features.T, aspect='auto', cmap='viridis', extent=[0, len(signal) / sampling_rate, 0, frame_size])
    plt.colorbar()
    plt.title("Cepstral Coefficients")
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
