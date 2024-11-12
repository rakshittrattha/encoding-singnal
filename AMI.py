import matplotlib.pyplot as plt
import numpy as np

# Function for AMI (Alternate Mark Inversion) Encoding
def encode_ami(bitstream):
    encoded_signal = []
    current_polarity = 1  # Initial polarity for '1' bits

    for bit in bitstream:
        if bit == '0':
            # A '0' bit is represented as 0 (no signal)
            encoded_signal.append(0)
        elif bit == '1':
            # A '1' bit alternates between positive and negative levels
            encoded_signal.append(current_polarity)
            current_polarity = -current_polarity  # Invert polarity for next '1'

    return encoded_signal

# Function to find the longest palindrome substring in a given string
def find_longest_palindrome(s):
    longest_palindrome_substring = ''
    n = len(s)
    
    # Create a 2D table to store results of subproblems
    dp_table = [[False] * n for _ in range(n)]
    
    # All single characters are palindromes
    for i in range(n):
        dp_table[i][i] = True
        longest_palindrome_substring = s[i]
    
    # Check for substrings of length greater than 1
    for start in range(n - 1, -1, -1):  # start from last character
        for end in range(start + 1, n):
            if s[start] == s[end]:
                # If characters match, check if the substring between them is a palindrome
                if end - start == 1 or dp_table[start + 1][end - 1]:
                    dp_table[start][end] = True
                    if len(longest_palindrome_substring) < len(s[start:end + 1]):
                        longest_palindrome_substring = s[start:end + 1]
    
    return longest_palindrome_substring

# Function to plot the AMI encoded signal
def plot_ami_signal(ami_signal):
    # Extend the last value to visualize the final bit properly
    extended_signal = ami_signal + [ami_signal[-1]]
    
    # Plot the AMI signal using a step plot
    plt.step(range(len(extended_signal)), extended_signal, where='post', color='blue', linewidth=2)
    plt.title('AMI Encoded Signal')
    plt.xlabel('Bit Index')
    plt.ylabel('Signal Level')
    plt.axhline(0, color='red', linestyle='-')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for clarity
    
    # Add grid lines for each bit position
    for i in range(len(ami_signal)):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)
    
    plt.show()

# Main code execution
input_data = input("Enter binary data: ")
ami_encoded_signal = encode_ami(input_data)
longest_palindrome = find_longest_palindrome(input_data)

print("Input Binary Data:", list(input_data))
print("AMI Encoded Signal:", ami_encoded_signal)
print("Longest Palindromic Substring in the Input Data: ", longest_palindrome)

# Plot the AMI encoded signal
plot_ami_signal(ami_encoded_signal)
