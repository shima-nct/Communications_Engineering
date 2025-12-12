import numpy as np
from scipy.signal import butter, lfilter, filtfilt

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    # Using filtfilt as per the fix
    y = filtfilt(b, a, data)
    return y

def run_verification():
    print("Running verification for OOK Modulation (Fixed Version)...")
    
    # Parameters matching the notebook
    sr = 22050
    delta_y = 0.05
    skip_t = 5
    fc = 8000
    
    # Generate synthetic bits
    n_bits = 1000
    bits_original = np.random.randint(0, 2, n_bits)
    
    # Create baseband signal b (upsampled)
    b = np.repeat(bits_original, skip_t)
    
    # Time vector
    t = np.linspace(0, len(b)/sr, len(b))
    
    # Carrier
    carrier = np.cos(2 * np.pi * fc * t)
    
    # Modulation
    ook_signal = b * carrier
    
    # Demodulation
    # 1. Rectification
    rectified = np.abs(ook_signal)
    
    # 2. LPF (using the fixed function with filtfilt)
    cutoff = 4500
    envelope = butter_lowpass_filter(rectified, cutoff, sr, order=6)
    
    # 3. Thresholding
    threshold = 0.5
    b_recovered = (envelope > threshold).astype(int)
    
    # Calculate BER
    # Sample at the middle of each skip_t block for robust symbol checking
    sample_indices = np.arange(skip_t // 2, len(b), skip_t)
    bits_rec = b_recovered[sample_indices]
    
    ber = np.mean(bits_original != bits_rec)
    
    print(f"Bit Error Rate (BER): {ber:.4f}")
    
    if ber == 0.0:
        print("SUCCESS: Decoding is perfect.")
    else:
        print("FAILURE: Bit errors detected.")

if __name__ == "__main__":
    run_verification()
