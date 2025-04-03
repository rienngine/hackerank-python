def swap_case(s):
    for char in s:
            if char.islower():
                s = s.replace(char, char.upper())
            elif char.isupper():
                s = s.replace(char, char.lower())     
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)