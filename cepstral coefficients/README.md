# Audio Cepstral Analysis

This project performs cepstral analysis on an audio signal and visualizes both the original audio signal and its cepstral coefficients.

## Requirements

To run this project, you need to have Python installed along with the following libraries:

- numpy
- librosa
- matplotlib

## Installation

1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Place your audio file in the project directory and update the `file_path` variable in the script to point to your audio file.
2. Run the script:

```bash
python audio_analysis.py
```

3. The script will display the original audio signal and its cepstral coefficients plot.

## Notes

- The audio file should be in WAV format.
- The script uses a frame size of 512 samples and an overlap of 256 samples for cepstral analysis.
- The sampling rate is set to 16000 Hz.

## License

This project is licensed under the MIT License.
```bash
### requirements.txt
```
the modules used : 
numpy
librosa
matplotlib
- Copy the following content:
     ```bash
     numpy
     librosa
     matplotlib
     ```
     and installation command using requirements.txt:
     ```bash
       pip install -r requirements.txt
     ```
## Usage
  first download it:
       ```
       git clone https://github.com/abolfazlsli/Language-and-Speech-Processing.git
       ```
  and the run by python !
# Output


![Figure_1](https://github.com/user-attachments/assets/9b411b9e-767a-442c-931f-49863c9c96ad)



