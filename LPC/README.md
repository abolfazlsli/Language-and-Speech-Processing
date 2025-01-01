# Linear Predictive Coding (LPC) Analysis

This project implements Linear Predictive Coding (LPC) to analyze and synthesize audio signals. LPC is a powerful technique used in speech processing and audio analysis, allowing for efficient representation of the spectral envelope of a signal.

## Overview

The main components of this project include:

- **Audio File Reading**: The project reads an audio file in WAV format.
- **LPC Coefficient Calculation**: LPC coefficients are computed from the audio signal.
- **Signal Synthesis**: A synthesized signal is generated using the LPC coefficients and a random excitation signal.
- **Visualization**: The original and synthesized signals are visualized using Matplotlib.

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

1. **`lpc(signal, order)`**: 
   - Computes the LPC coefficients for the input signal.
   - Uses autocorrelation to estimate the coefficients based on the specified order.
   - Constructs the autocorrelation matrix and applies the Levinson-Durbin algorithm to solve for the LPC coefficients.

### Main Code Execution

- The audio file is read using `scipy.io.wavfile.read()`.
- If the audio data is stereo (2D array), it selects the first channel.
- The audio data is normalized to ensure that the values are between -1 and 1.
- The LPC coefficients are calculated using the `lpc()` function with a specified order (12 in this case).
- A random excitation signal is generated to synthesize the audio.
- The synthesized signal is created using the `lfilter()` function, which applies the LPC coefficients to the excitation signal.

### Visualization

The resulting plot displays both the original and synthesized signals:
- The top panel shows the original audio signal.
- The bottom panel shows the synthesized signal generated from the LPC coefficients.

## Running the Code

To run the code, ensure you have a WAV audio file named `15-15- amozesh dadan.wav` in the same directory as the script. Then execute the script:

```bash
python lpc_analysis.py
```

Make sure to replace `lpc_analysis.py` with the actual filename if it's different.

## Conclusion

This project provides a basic implementation of Linear Predictive Coding, which can be useful for speech synthesis and audio analysis tasks. You can experiment with different audio files and LPC orders to see how they affect the synthesized output.

Feel free to modify the code and explore further applications of LPC!