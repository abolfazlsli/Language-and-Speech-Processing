# Signal and FFT Analysis

This repository provides a Python script to analyze and visualize a composite signal in both the time domain and frequency domain using the Fast Fourier Transform (FFT).

## Features
- Generates a composite signal consisting of a sine wave and a square wave.
- Computes the FFT of the signal to identify frequency components.
- Displays the signal in both time domain and frequency domain.

## Installation
To use this script, ensure you have Python 3.7+ installed along with the required libraries. Install dependencies using:

```bash
pip install -r requirements.txt
```

## Usage
1. Run the Python script:

```bash
python signal_fft_analysis.py
```

2. The script will generate two plots:
   - The time-domain representation of the signal.
   - The frequency-domain representation (FFT) showing the magnitude of frequency components.

## Dependencies
- Python 3.7+
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

## Repository Structure
```
Signal-FFT-Analysis/
├── signal_fft_analysis.py    # Main script
├── requirements.txt          # Required dependencies
└── README.md                 # Documentation
```

## Example Output
The script generates the following visualizations:
1. **Time Domain Signal**: Shows the composite waveform over time.
2. **Frequency Domain (FFT)**: Highlights the primary frequency components of the signal.

![Figure_1](https://github.com/user-attachments/assets/75f74553-3cd3-4153-b502-5dfd2dc13239)


## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
