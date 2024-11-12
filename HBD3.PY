import matplotlib.pyplot as plt

# HDB3 Encoding Function
def encode_hdb3(bitstream):
    encoded_signal = []
    zero_counter = 0
    last_substitution_counter = 0
    current_polarity = 1

    for bit in bitstream:
        if bit == '1':
            # Toggle voltage polarity for each '1' bit
            encoded_signal.append(current_polarity)
            current_polarity = -current_polarity
            zero_counter = 0
            last_substitution_counter = 0
        else:  # Handle the '0' bit
            zero_counter += 1
            if zero_counter == 4:
                # Perform substitution for four consecutive '0's
                encoded_signal[-3:] = []  # Remove the last three zeros

                # Apply substitution rule based on the number of previous substitutions
                if last_substitution_counter % 2 == 0:
                    encoded_signal.extend([-current_polarity, 0, 0, -current_polarity])
                else:
                    encoded_signal.extend([0, 0, 0, -current_polarity])

                last_substitution_counter += 1
                zero_counter = 0
            else:
                encoded_signal.append(0)  # Maintain zero level for non-consecutive zeros

    return encoded_signal

# Function to Find the Longest Palindrome Substring
def find_longest_palindrome_substring(input_string):
    max_palindrome = ''
    n = len(input_string)

    # Create a table to store palindrome truth values for substrings
    dp_table = [[False] * n for _ in range(n)]

    # Every single character is a palindrome by itself
    for i in range(n):
        dp_table[i][i] = True
        max_palindrome = input_string[i]

    # Check for substrings longer than one character
    for start in range(n - 1, -1, -1):  # Traverse from end to start
        for end in range(start + 1, n):
            if input_string[start] == input_string[end]:
                # Check if the substring between start and end is a palindrome
                if end - start == 1 or dp_table[start + 1][end - 1]:
                    dp_table[start][end] = True
                    if len(max_palindrome) < len(input_string[start:end + 1]):
                        max_palindrome = input_string[start:end + 1]

    return max_palindrome

# Main Execution
input_data = input("Enter the binary data stream: ")
hdb3_encoded_data = encode_hdb3(input_data)
longest_palindrome_in_stream = find_longest_palindrome_substring(input_data)

print("Binary Data Stream:", list(input_data))
print("HDB3 Encoded Signal:", hdb3_encoded_data)
print("Longest Palindromic Substring in Data Stream:", longest_palindrome_in_stream)

# Plotting the HDB3 Encoded Data
def plot_hdb3_encoded_signal(encoded_data):
    time_vector = range(len(encoded_data))

    plt.step(time_vector, encoded_data, where='post', color='blue', linewidth=2)
    plt.title('HDB3 Encoded Signal')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red', linestyle='-')  # Zero line for reference
    plt.ylim(-1.5, 1.5)  # Set y-axis limits to visualize voltage levels
    plt.xlim(0, len(encoded_data) - 1)  # Ensure x-axis starts at 0

    # Add vertical lines to indicate bit transitions
    for idx in range(0, len(encoded_data), 2):
        plt.axvline(idx, color='gray', linestyle='--', linewidth=0.5)

    plt.show()

plot_hdb3_encoded_signal(hdb3_encoded_data)
