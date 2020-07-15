'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    if len(arr) <= 1:
        return 0
    
    dupes = []

    for x in arr:
        if x not in dupes:
            dupes.append(x)
            arr.remove(x)
        
    for y in dupes:
        if y not in arr:
            return y



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")




