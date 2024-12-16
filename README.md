# Signal Processing Algorithms Collection

This repository contains a collection of Python scripts implementing various signal processing algorithms. These algorithms are useful for frequency analysis, cepstral processing, spectral guarantees, and other signal-related tasks.

## Algorithms
1. **AMDF**  
   Implements the Average Magnitude Difference Function (AMDF) algorithm, commonly used for pitch detection and periodicity analysis.

2. **cepstral coefficients**  
   Contains algorithms for calculating cepstral coefficients, which are widely used for speech processing and audio feature extraction.

3. **CQT**  
   Implements the Constant-Q Transform (CQT), useful for analyzing signals in the frequency domain with logarithmic scaling.

4. **FFT**  
   Provides algorithms for Fast Fourier Transform (FFT), a core technique for converting signals from the time domain to the frequency domain.

5. **Cepstral**  
   Computes the cepstral features of a signal, typically used for speech recognition and audio signal characterization.

6. **HPS**  
   Implements the Harmonic Product Spectrum (HPS) algorithm, an efficient method for estimating the fundamental frequency of a signal.

7. **LPC**  
   Linear Predictive Coding (LPC) algorithm for spectral envelope estimation and audio signal compression.

8. **Spectral Guarantee**  
   Ensures specific spectral properties in a signal, useful for noise reduction or spectral adjustments.

9. **Step Guarantee**  
   Implements a step detection or step adjustment algorithm for signal analysis or correction.

## Installation
1. Ensure you have Python 3.7+ installed.
2. Install required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/signal-processing-algorithms.git
   cd signal-processing-algorithms
   ```
2. Run any algorithm script:
   ```bash
   python script_name.py
   ```

## Repository Structure
```
Signal-Processing-Algorithms/
├── AMDF/                         # AMDF Algorithm
├── cepstral coefficients/        # Cepstral Coefficients Algorithm
├── CQT/                          # Constant-Q Transform Algorithm
├── FFT/                          # FFT Algorithm
├── Cepstral.py                   # Cepstral Features Algorithm
├── HPS/                          # Harmonic Product Spectrum Algorithm
├── LPC/                          # Linear Predictive Coding Algorithm
├── Spectral Guarantee/           # Spectral Guarantee Algorithm
├── Step Guarantee/               # Step Guarantee Algorithm
├── requirements.txt              # Required Libraries
└── README.md                     # Documentation
```

## Visual Overview
Below is a visual summary of the algorithms implemented in this repository:

| ![Algorithm 1](path/to/image1.png) | ![Algorithm 2](path/to/image2.png) |
|:----------------------------------:|:----------------------------------:|
| Algorithm 1 Description            | Algorithm 2 Description            |

| ![Algorithm 3](path/to/image3.png) | ![Algorithm 4](path/to/image4.png) |
|:----------------------------------:|:----------------------------------:|
| Algorithm 3 Description            | Algorithm 4 Description            |

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
