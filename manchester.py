import matplotlib.pyplot as plt

# Manchester Encoding Function
def encode_manchester(bits):
    encoded_signal = []
    for bit in bits:
        if bit == '0':
            # Encode binary 0 as a high-to-low transition
            encoded_signal.extend([1, -1])
        elif bit == '1':
            # Encode binary 1 as a low-to-high transition
            encoded_signal.extend([-1, 1])
    return encoded_signal

# Longest Palindromic Substring Finder Function
def longest_palindrome(s):
    longest_palindrome = ''
    dp = [[False] * len(s) for _ in range(len(s))]

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

# Main Program Execution
if __name__ == '__main__':
    # User Input for Binary Data
    binary_data = input("Enter the binary data: ")
    
    # Encode the binary data using Manchester encoding
    encoded_data = encode_manchester(binary_data)
    
    # Find the longest palindrome in the binary data stream
    palindrome = longest_palindrome(binary_data)

    # Output the results
    print("Binary Data:", list(binary_data))
    print("Manchester Encoded Data:", encoded_data)
    print("Longest Palindromic Substring in Data Stream:", palindrome)

    # Plotting the Manchester Encoded Signal
    def plot_encoded_signal(encoded_data):
        # Create time axis based on the number of bits
        time_axis = range(len(encoded_data))

        # Create the step plot
        plt.step(time_axis, encoded_data, where='post', color='blue', linewidth=2)
        plt.title('Manchester Encoded Signal')
        plt.xlabel('Bit Index')
        plt.ylabel('Signal Level')
        plt.axhline(0, color='red', linestyle='-')  # Zero level reference line
        plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
        plt.xlim(0, len(encoded_data) - 1)  # Ensure x-axis starts from 0

        # Add vertical lines at each bit transition for better clarity
        for idx in range(0, len(encoded_data), 2):
            plt.axvline(idx, color='gray', linestyle='--', linewidth=0.5)

        # Show the plot
        plt.show()

    # Plot the encoded Manchester signal
    plot_encoded_signal(encoded_data)
