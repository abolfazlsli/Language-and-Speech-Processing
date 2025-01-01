# Cepstral Analysis of a Signal

This project implements cepstral analysis on a synthetic signal using Python. The analysis is performed using the Fast Fourier Transform (FFT) to extract cepstral coefficients, which are useful in various applications such as speech processing and audio analysis.

## Overview

The main components of this project include:

- **Signal Generation**: A synthetic signal is created by combining two sine waves of different frequencies.
- **Cepstral Analysis**: The signal is divided into overlapping frames, and cepstral coefficients are computed for each frame.
- **Visualization**: The original signal and the computed cepstral coefficients are visualized using Matplotlib.

## Requirements

To run this project, you need to have the following Python packages installed:

- `numpy`
- `matplotlib`

You can install the required packages using pip:

```bash
pip install numpy matplotlib
```

## Code Explanation

### Functions

1. **`create_signal()`**: 
   - Generates a synthetic signal composed of two sine waves (100 Hz and 200 Hz) sampled at 1000 Hz.

2. **`cepstral_analysis(signal, frame_size, overlap, sampling_rate)`**: 
   - Performs cepstral analysis on the input signal.
   - Divides the signal into overlapping frames.
   - Computes the FFT of each frame, takes the logarithm of the magnitude spectrum, and then computes the inverse FFT to obtain the cepstral coefficients.

3. **`main()`**: 
   - Calls the `create_signal()` function to generate the signal.
   - Defines frame size and overlap for cepstral analysis.
   - Calls the `cepstral_analysis()` function to compute cepstral features.
   - Plots the original signal and the cepstral coefficients.

### Visualization

The results are displayed in a two-panel plot:
- The top panel shows the original signal.
- The bottom panel displays the cepstral coefficients as a heatmap, where the x-axis represents time and the y-axis represents the cepstral coefficients.

## Running the Code

To run the code, simply execute the script:

```bash
python cepstral_analysis.py
```

Make sure to replace `cepstral_analysis.py` with the actual filename if it's different.

## Conclusion

This project provides a basic implementation of cepstral analysis, which can be extended for more complex signals and applications. The cepstral coefficients can be further used for tasks such as feature extraction in speech recognition or audio classification.

Feel free to modify the parameters and explore the effects on the cepstral coefficients!