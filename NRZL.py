import matplotlib.pyplot as plt

# NRZ-L (Non Return to Zero-Level) Encoding Function
def nrz_l_encoding(bits):
    """Encodes the bitstream using NRZ-L encoding."""
    encoded_data = []
    for bit in bits:
        # '1' is represented by high voltage (1), '0' by low voltage (-1)
        encoded_data.append(1 if bit == '1' else -1)
    # Extend the last voltage level for visualization purposes
    encoded_data.append(encoded_data[-1])
    return encoded_data

# Longest Palindromic Substring Finder
def longest_palindrome(s):
    """Finds the longest palindromic substring in the input string."""
    longest_palindrome = ''
    dp = [[False] * len(s) for _ in range(len(s))]
    
    # Every single character is a palindrome by itself
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrome = s[i]

    # Check for palindromes of length 2 and greater
    for length in range(2, len(s) + 1):
        for i in range(len(s) - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if len(longest_palindrome) < length:
                    longest_palindrome = s[i:j + 1]
    
    return longest_palindrome

# Plotting NRZ-L Encoded Data
def plot(nrz_l_data):
    """Plots the NRZ-L encoded signal."""
    plt.step(range(len(nrz_l_data)), nrz_l_data, where='post', color='red', linewidth=2)
    plt.title('NRZ-L Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='blue', linestyle='--')  # Reference zero line
    plt.ylim(-1.5, 1.5)
    
    # Add vertical dashed lines at each bit transition for better visualization
    for i in range(len(nrz_l_data)):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)
    
    # Display the plot
    plt.show()

# Main Execution
if __name__ == '__main__':
    # User input for binary data
    binary_bits = input("Enter the binary data: ")

    # Perform NRZ-L encoding
    nrz_l_data = nrz_l_encoding(binary_bits)
    
    # Find the longest palindromic substring in the binary data
    palindrome = longest_palindrome(binary_bits)

    # Output the results
    print("Binary Data:", list(binary_bits))
    print("NRZ-L Encoded Data:", nrz_l_data)
    print("Longest Palindromic Substring in Data Stream:", palindrome)

    # Plot the NRZ-L encoded data
    plot(nrz_l_data)
