# Read an integer 'n' from STDIN.
# Print the integers from 1 to 'n' consecutively as a single string.
# Constraints: Do not use string methods for formatting.
# Example: If n = 5, output should be "12345".

if __name__ == '__main__':
    n = int(input())
    
    for x in range(1, n + 1):
        print(x, end="") # Just change the default output separator to an empty string