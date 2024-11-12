import matplotlib.pyplot as plt

# NRZ-I Encoding function
def nrz_i_encoding(bits):
    encoded_bits = []
    current_level = 1  # Start with high level for NRZ-I

    for bit in bits:
        if bit == '1':
            current_level = -current_level  # Invert the level for '1'
        encoded_bits.append(current_level)
    return encoded_bits

# Longest Palindromic Substring Finder
def longest_palindrome(s):
    longest_palindrome = ''
    dp = [[False]*len(s) for _ in range(len(s))]

    # Every single character is a palindrome by itself
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrome = s[i]

    # Check substrings of length 2 to len(s)
    for length in range(2, len(s) + 1):
        for i in range(len(s) - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if len(longest_palindrome) < length:
                        longest_palindrome = s[i:j+1]

    return longest_palindrome

# Plotting NRZ-I Encoded Data
def plot_nrz_i(nrz_i_data):
    # Extend the data by duplicating the last value for visualization purposes
    extended_data = nrz_i_data + [nrz_i_data[-1]]
    
    # Create the step plot
    plt.step(range(len(extended_data)), extended_data, where='post', color='red', linewidth=2)
    plt.title('NRZ-I Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='blue', linestyle='--')  # Reference zero line
    plt.ylim(-1.5, 1.5)
    
    # Add vertical lines for each bit transition for better visualization
    for i in range(len(nrz_i_data)):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)
    
    # Display the plot
    plt.show()

# Main Execution
if __name__ == '__main__':
    # User input for binary data
    binary_bits = input("Enter the binary data: ")
    
    # Perform NRZ-I encoding
    nrz_i_data = nrz_i_encoding(binary_bits)
    
    # Find the longest palindromic substring in the binary data
    palindrome = longest_palindrome(binary_bits)

    # Output the results
    print("Binary Data:", list(binary_bits))
    print("NRZ-I Encoded Data:", nrz_i_data)
    print("Longest Palindromic Substring in Data Stream:", palindrome)

    # Plot the NRZ-I encoded data
    plot_nrz_i(nrz_i_data)
