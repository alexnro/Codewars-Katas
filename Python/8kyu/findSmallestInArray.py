def find_smallest_int(arr):
    result = arr[0]
    for num in arr:
        if num < result:
            result = num
    return result

# Other solution
# def find_smallest_int(arr):
#     orderArr = arr.sort()
#     return arr[0]



if __name__ == "__main__":
    
    assert find_smallest_int([78, 56, 232, 12, 11, 43]) == 11
    assert find_smallest_int([78, 56, -2, 12, 8, -33]) == -33
    assert find_smallest_int([0, 1-2**64, 2**64]) == 1-2**64