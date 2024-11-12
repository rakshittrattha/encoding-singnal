import matplotlib.pyplot as plt

# Function for B8ZS (Bipolar 8-Zero Substitution) Encoding
def encode_b8zs(bits):
    encoded_signal = []
    zero_count = 0
    current_polarity = 1  # Initial polarity for '1' bits

    for bit in bits:
        if bit == '1':
            encoded_signal.append(current_polarity)
            zero_count = 0
            current_polarity = -current_polarity  # Alternate polarity for subsequent '1'
        elif bit == '0':
            zero_count += 1
            if zero_count == 8:
                # Substitution pattern for 8 consecutive zeros
                # Substitutes: 000VB0VB (V = voltage level, B = bipolar sign change)
                for _ in range(7):  # Remove the last 7 zeros
                    encoded_signal.pop()
                encoded_signal.extend([0, 0, 0, -current_polarity, current_polarity, 0, current_polarity, -current_polarity])
                zero_count = 0  # Reset zero counter after substitution
            else:
                encoded_signal.append(0)  # Append zero for each '0' bit

    # Append the last voltage level for completeness in the graph
    encoded_signal.append(encoded_signal[-1])
    return encoded_signal


# Function to find the longest palindrome in a string
def find_longest_palindrome(substring):
    longest_palindrome = ''
    n = len(substring)

    # Create a table to store palindrome results
    dp_table = [[False] * n for _ in range(n)]

    # Every single character is a palindrome by itself
    for i in range(n):
        dp_table[i][i] = True
        longest_palindrome = substring[i]

    # Check substrings of increasing lengths
    for start in range(n - 1, -1, -1):  # Start from the end of the string
        for end in range(start + 1, n):
            if substring[start] == substring[end]:
                if end - start == 1 or dp_table[start + 1][end - 1]:
                    dp_table[start][end] = True
                    if len(longest_palindrome) < len(substring[start:end + 1]):
                        longest_palindrome = substring[start:end + 1]

    return longest_palindrome


# Function to visualize the B8ZS encoded signal
def plot_b8zs_signal(encoded_bits):
    # Extend the signal for proper graphing
    extended_signal = encoded_bits + [encoded_bits[-1]]

    # Plot the encoded signal using a step plot
    plt.step(range(len(extended_signal)), extended_signal, where='post', color='blue', linewidth=2)
    plt.title('B8ZS Encoded Signal')
    plt.xlabel('Bit Index')
    plt.ylabel('Signal Level')
    plt.axhline(0, color='red', linestyle='-')  # Zero reference line
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization

    # Add grid lines for each bit index
    for i in range(len(encoded_bits)):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)

    plt.show()


# Main Execution Flow
input_data = input("Enter the binary data: ")
b8zs_encoded_signal = encode_b8zs(input_data)
longest_palindrome = find_longest_palindrome(input_data)

# Output the results
print("Input Binary Data:", list(input_data))
print("B8ZS Encoded Signal:", b8zs_encoded_signal)
print("Longest Palindromic Substring:", longest_palindrome)

# Plotting the B8ZS encoded signal
plot_b8zs_signal(b8zs_encoded_signal)
