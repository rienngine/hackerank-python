if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))  # max() generates an iterable object, so we need to convert it to a list
    
    highest = max(arr)
    new_arr = [i for i in arr if i != highest] # I opted for list comprehensions here
    runner_up = max(new_arr)
    
    print(runner_up)