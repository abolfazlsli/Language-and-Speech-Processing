# Constant-Q Transform (CQT) Visualization

This repository provides a Python script to visualize the Constant-Q Transform (CQT) of an audio file. The CQT is displayed as a spectrogram, showing the amplitude in decibels over time and frequency.

## Features
- Load an audio file and compute its CQT using [Librosa](https://librosa.org/).
- Convert the CQT amplitude to decibels.
- Plot the CQT spectrogram with labeled axes and a color bar.

## Installation
To use this script, install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage
1. Place your audio file (e.g., `15-15- amozesh dadan.wav`) in the `audio` directory.
2. Run the Python script:

```bash
python scripts/cqt_visualization.py
```

3. The CQT spectrogram will be displayed.

## Dependencies
- Python 3.7+
- [NumPy](https://numpy.org/)
- [Librosa](https://librosa.org/)
- [Matplotlib](https://matplotlib.org/)


## Example Output
An example visualization of a CQT spectrogram will look like this:
![Figure_1](https://github.com/user-attachments/assets/76d585ca-2453-4a8e-8f73-0585d33c3208)



## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
