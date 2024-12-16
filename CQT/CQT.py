import numpy as np
import librosa
import matplotlib.pyplot as plt


file_path = './15-15- amozesh dadan.wav'
y, sr = librosa.load(file_path)

cqt = librosa.cqt(y, sr=sr, n_bins=84, bins_per_octave=12)

cqt_db = librosa.amplitude_to_db(np.abs(cqt), ref=np.max)

plt.figure(figsize=(12, 6))
librosa.display.specshow(cqt_db, sr=sr, x_axis='time', y_axis='cqt_hz', bins_per_octave=12)
plt.colorbar(label='Amplitude (dB)')
plt.title('Constant-Q Transform (CQT)')
plt.tight_layout()
plt.show()
