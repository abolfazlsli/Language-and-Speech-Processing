# Spectral Analysis of an Audio Signal

This project performs a spectral analysis of an audio signal using the Fast Fourier Transform (FFT). The analysis provides insights into the frequency components of the audio, which can be useful for various applications such as audio processing, music analysis, and speech recognition.

## Overview

The main components of this project include:

- **Audio File Reading**: The project reads an audio file in WAV format.
- **FFT Calculation**: The FFT is computed to transform the audio signal from the time domain to the frequency domain.
- **Magnitude Spectrum Visualization**: The magnitude of the frequency components is visualized using Matplotlib.

## Requirements

To run this project, you need to have the following Python packages installed:

- `numpy`
- `matplotlib`
- `scipy`

You can install the required packages using pip:

```bash
pip install numpy matplotlib scipy
```

## Code Explanation

### Main Code Execution

1. **Reading the Audio File**:
   - The audio file is read using `scipy.io.wavfile.read()`, which returns the sample rate and the audio data.

2. **FFT Calculation**:
   - The FFT of the audio data is computed using `np.fft.fft()`, which transforms the signal into the frequency domain.
   - The frequency bins are generated using `np.fft.fftfreq()`, which provides the corresponding frequencies for the FFT output.

3. **Magnitude Spectrum**:
   - The magnitude of the spectrum is calculated using `np.abs()`, which gives the absolute values of the complex FFT output.
   - Negative values in the spectrum are set to zero to ensure a non-negative magnitude spectrum.

4. **Visualization**:
   - The resulting plot displays the magnitude spectrum:
     - The x-axis represents frequency in Hertz (Hz).
     - The y-axis represents the magnitude of the frequency components.
     - The plot is limited to half the sample rate (Nyquist frequency) for clarity.

### Visualization Code

```python
plt.figure(figsize=(12, 6))
plt.plot(frequency, np.abs(spectrum))
plt.title('Spectral Analysis')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, sample_rate / 2)
plt.grid()
plt.show()
```

## Running the Code

To run the code, ensure you have a WAV audio file named `Mehrad Hidden - Rakab.wav` in the same directory as the script. Then execute the script:

```bash
python spectral_analysis.py
```

Make sure to replace `spectral_analysis.py` with the actual filename if it's different.

## Conclusion

This project provides a basic implementation of spectral analysis using the Fast Fourier Transform. The resulting magnitude spectrum can be used to analyze the frequency content of the audio signal, which is valuable for various audio processing tasks.

Feel free to modify the code and explore further applications of spectral analysis!