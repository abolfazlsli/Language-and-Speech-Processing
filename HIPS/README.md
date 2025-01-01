# Harmonic Product Spectrum Analysis

This project implements the Harmonic Product Spectrum (HPS) method to analyze audio signals. The HPS technique is commonly used in pitch detection and music analysis, as it helps to identify the fundamental frequency of a sound by emphasizing harmonic frequencies.

## Overview

The main components of this project include:

- **Audio File Reading**: The project reads an audio file in WAV format.
- **Harmonic Product Spectrum Calculation**: The HPS is computed from the audio signal to extract the harmonic content.
- **Visualization**: The resulting HPS is visualized using Matplotlib.

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

### Functions

1. **`hps(signal, sample_rate, max_harmonics=5)`**: 
   - Computes the Harmonic Product Spectrum of the input signal.
   - Takes the FFT of the signal to obtain the frequency spectrum.
   - Iteratively down-samples the spectrum for each harmonic and multiplies it with the original spectrum to emphasize the fundamental frequency.

### Main Code Execution

- The audio file is read using `scipy.io.wavfile.read()`.
- If the audio data is stereo (2D array), it selects the first channel.
- The audio data is normalized to ensure that the values are between -1 and 1.
- The HPS is calculated using the `hps()` function.
- The frequency bins are generated using `np.fft.fftfreq()`.
- The HPS result is plotted against the frequency using Matplotlib.

### Visualization

The resulting plot displays the Harmonic Product Spectrum:
- The x-axis represents frequency in Hertz (Hz).
- The y-axis represents the magnitude of the HPS.
- The plot is limited to half the sample rate (Nyquist frequency) for clarity.

## Running the Code

To run the code, ensure you have a WAV audio file named `Mehrad Hidden - Rakab.wav` in the same directory as the script. Then execute the script:

```bash
python harmonic_product_spectrum.py
```

Make sure to replace `harmonic_product_spectrum.py` with the actual filename if it's different.

## Conclusion

This project provides a basic implementation of the Harmonic Product Spectrum analysis, which can be useful for pitch detection and audio analysis tasks. You can experiment with different audio files and the `max_harmonics` parameter to see how it affects the HPS results.

Feel free to modify the code and explore further applications of the Harmonic Product Spectrum!