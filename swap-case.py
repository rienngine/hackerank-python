# Convert all lowercase characters in a string to uppercase, and all uppercase characters to lowercase.
# Example: Input "HeLLo" -> Output "hEllO".

''' (First try)
def swap_case(s):
    for c in range(len(s)):
            if s[c].isupper():
                s = s[:c] + s[c].lower() + s[c+1:]
            elif s[c].islower():
                s = s[:c] + s[c].upper() + s[c+1:]
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''

# For this specific case, simply use swapcase() method.

def swap_case(s):
    return s.swapcase()

s = input()
result = swap_case(s)
print(result)