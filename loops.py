# Print the square of all non-negative integers less than n

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n): # To be able to iterate from 0 to n - 1
        print(i ** 2)