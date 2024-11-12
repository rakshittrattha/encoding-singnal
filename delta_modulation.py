import numpy as np
import matplotlib.pyplot as plt

# Input Parameters
sampling_freq = float(input("Enter the sampling frequency: "))
duration = float(input("Enter the duration of the signal (seconds): "))
time_vector = np.arange(duration * sampling_freq) / sampling_freq

# Signal Component Frequencies and Amplitudes
cosine_freq = float(input("Enter the frequency of the cosine component (Hz): "))
sine_freq = float(input("Enter the frequency of the sine component (Hz): "))
cosine_amplitude = float(input("Enter the amplitude of the cosine component: "))
sine_amplitude = float(input("Enter the amplitude of the sine component: "))

# Signal Generation (Cosine + Sine)
cosine_wave = cosine_amplitude * np.cos(2 * np.pi * cosine_freq * time_vector)
sine_wave = sine_amplitude * np.sin(2 * np.pi * sine_freq * time_vector)
combined_signal = cosine_wave + sine_wave

# Signal Bandwidth and Delta Modulation Sampling Frequency
signal_bandwidth = max(cosine_freq, sine_freq)
nyquist_rate = float(input("Enter the Nyquist rate (samples/second): "))
dm_sampling_freq = nyquist_rate * 2 * signal_bandwidth
step_size = float(input("Enter the step size (epsilon) for delta modulation: "))

# Delta Modulation Signal Sampling
dm_time_vector = np.arange(duration * dm_sampling_freq) / dm_sampling_freq
sampled_cosine = cosine_amplitude * np.cos(2 * np.pi * cosine_freq * dm_time_vector)
sampled_sine = sine_amplitude * np.sin(2 * np.pi * sine_freq * dm_time_vector)
sampled_combined_signal = sampled_cosine + sampled_sine

# Delta Modulation Encoding
predicted_signal = np.zeros(len(sampled_combined_signal)) 
encoded_signal = np.zeros_like(predicted_signal)

for i in range(1, len(sampled_combined_signal)):
    amplitude_difference = sampled_combined_signal[i] - predicted_signal[i - 1]
    encoded_signal[i] = (2 * int(amplitude_difference > 0) - 1) * step_size
    predicted_signal[i] = predicted_signal[i - 1] + encoded_signal[i]

# Plotting Results
plt.figure(figsize=(20, 15))
display_duration = 0.1

# First Plot - Original vs Delta-Modulated Signal
plt.subplot(3, 1, 1)
plt.plot(time_vector, combined_signal, color='black', label='Original Signal')
plt.step(dm_time_vector, predicted_signal, color='red', where='post', label='Delta-Modulated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original and Delta-Modulated Signals')
plt.legend()
plt.xlim(0, display_duration)
plt.ylim(min(combined_signal) - 0.5, max(combined_signal) + 0.5)
plt.xticks(np.arange(0, display_duration, display_duration / 10))
plt.grid()

# Second Plot - Delta Modulation Output
plt.subplot(3, 1, 2)
plt.stem(dm_time_vector, encoded_signal, linefmt='r', markerfmt='ro', basefmt='k')
plt.xlabel('Time (s)')
plt.ylabel('Step Amplitude')
plt.title('Delta Modulation Output')
plt.xlim(0, display_duration)
plt.ylim(-2 * step_size, 2 * step_size)
plt.xticks(np.arange(0, display_duration, display_duration / 10))
plt.grid()

# Third Plot - Decoded Signal vs Original Message
plt.subplot(3, 1, 3)
plt.plot(time_vector, combined_signal, color='black', label='Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Decoded Signal vs Original Signal')
plt.legend()
plt.xlim(0, display_duration)
plt.ylim(min(combined_signal) - 0.5, max(combined_signal) + 0.5)
plt.xticks(np.arange(0, display_duration, display_duration / 10))
plt.grid()

plt.tight_layout()
plt.show()
