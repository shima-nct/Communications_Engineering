import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Simulate parameters
sr = 22050
duration = 0.1
t = np.linspace(0, duration, int(sr * duration))
# Create a dummy signal y (sine wave)
y = 0.5 * np.sin(2 * np.pi * 440 * t)

delta_y = 0.05
skip_t = 5

# Delta Modulation
z_ref = np.zeros(len(y))
b = np.zeros(len(y))
z_ref[0] = y[0]
b[0] = 0

for i in range(1, len(y)-1, skip_t): 
    diff = y[i] - z_ref[i-1]
    if diff < 0:
        z_ref[i] = z_ref[i-1] - delta_y
        b[i] = 0
    else:
        z_ref[i] = z_ref[i-1] + delta_y
        b[i] = 1

    for j in range(i+1, min(i+skip_t, len(y)-1)):
        z_ref[j] = z_ref[i]
        b[j] = b[i]

# OOK Modulation
fc = 8000
carrier = np.cos(2 * np.pi * fc * t)
ook_signal = b * carrier

# Demodulation
rectified = np.abs(ook_signal)

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

cutoff = 4500
envelope = butter_lowpass_filter(rectified, cutoff, sr, order=6)

threshold = 0.5
b_recovered = (envelope > threshold).astype(float)

# Compare b and b_recovered
# Calculate Bit Error Rate
ber = np.mean(np.abs(b - b_recovered))
print(f"Bit Error Rate: {ber:.4f}")

# Check if completely different
if ber > 0.1:
    print("FAIL: Decoded waveform is significantly different.")
else:
    print("SUCCESS: Decoded waveform matches.")
