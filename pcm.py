import numpy as np
import matplotlib.pyplot as plt

def pcm_encode(input_signal, quantization_levels):
    """
    Encode the input analog signal using PCM with the specified number of quantization levels.
    """
    # Normalize the signal to the range [0, 1]
    normalized_signal = (input_signal - np.min(input_signal)) / (np.max(input_signal) - np.min(input_signal))
    
    # Quantize the normalized signal into the specified number of levels
    quantized_output = np.round(normalized_signal * (quantization_levels - 1))
    
    return quantized_output

# User Inputs for signal properties
time = np.arange(0, 1, 0.001)
amplitude = float(input("Enter the signal amplitude: "))
frequency = float(input("Enter the signal frequency: "))
levels = int(input("Enter the number of quantization levels (e.g., 8): "))

# Generate a synthetic analog signal (sum of two sine waves with different frequencies)
analog_wave = amplitude * np.sin(2 * np.pi * frequency * time) + amplitude * np.sin(2 * np.pi * (2 * frequency) * time)

# Perform PCM encoding
encoded_signal = pcm_encode(analog_wave, levels)

# Plot the original and PCM encoded signals
plt.subplot(2, 1, 1)
plt.plot(time, analog_wave, color='blue')
plt.title('Original Analog Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.step(time, encoded_signal, color='orange', linewidth=1)
plt.title(f'PCM Quantized Signal (Levels: {levels})')
plt.xlabel('Time')
plt.ylabel('Quantized Level')

plt.tight_layout()
plt.show()

# Print the encoded quantized signal
print("Quantized Signal:", encoded_signal)
