import matplotlib.pyplot as plt

# Function for Differential Manchester Encoding
def encode_differential_manchester(bit_sequence):
    encoded_signal = []
    current_voltage_level = 1  # Initial voltage level

    for bit in bit_sequence:
        if bit == '0':  # '0' is represented by an inversion
            encoded_signal.extend([current_voltage_level, -current_voltage_level])
        elif bit == '1':  # '1' is represented by an inversion and a voltage change
            encoded_signal.extend([-current_voltage_level, current_voltage_level])
            current_voltage_level = -current_voltage_level  # Flip voltage level for the next bit

    return encoded_signal

# Function to find the longest palindromic substring in a given string
def find_longest_palindrome(s):
    max_palindrome = ''
    n = len(s)

    # Create a table to store whether substrings are palindromes
    dp_table = [[False] * n for _ in range(n)]

    # Every single character is a palindrome by itself
    for i in range(n):
        dp_table[i][i] = True
        max_palindrome = s[i]

    # Check for substrings longer than one character
    for start in range(n - 1, -1, -1):  # Start from the end of the string
        for end in range(start + 1, n):
            if s[start] == s[end]:
                # Check if the substring between start and end is a palindrome
                if end - start == 1 or dp_table[start + 1][end - 1]:
                    dp_table[start][end] = True
                    if len(max_palindrome) < len(s[start:end + 1]):
                        max_palindrome = s[start:end + 1]

    return max_palindrome

# Function to plot the Differential Manchester Encoded Signal
def plot_encoded_signal(encoded_data):
    extended_data = encoded_data + [encoded_data[-1]]  # Extend for proper plot visualization
    plt.step(range(len(extended_data)), extended_data, where='post', color='blue', linewidth=2)
    plt.title('Differential Manchester Encoded Signal')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red', linestyle='-')  # Reference line at zero voltage level
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for clarity

    # Draw vertical grid lines for each bit index
    for i in range(len(encoded_data)):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)

    plt.show()

# Main function execution
binary_data = input("Enter the binary sequence: ")
encoded_signal = encode_differential_manchester(binary_data)
longest_palindrome_in_stream = find_longest_palindrome(binary_data)

print("Binary Data:", list(binary_data))
print("Differential Manchester Encoded Signal:", encoded_signal)
print("Longest Palindrome in the Data Stream:", longest_palindrome_in_stream)

# Plotting the encoded signal
plot_encoded_signal(encoded_signal)
