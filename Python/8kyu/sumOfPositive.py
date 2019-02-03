def positive_sum(arr):
    result = 0
    for num in arr:
        if num > 0:
            result = result + num
        else:
            pass
    return result



if __name__ == "__main__":
    
    assert positive_sum([1,2,3,4,5]) == 15
    assert positive_sum([1,-2,3,4,5]) == 13
    assert positive_sum([-1,2,3,4,-5]) == 9
    assert positive_sum([]) == 0
    assert positive_sum([-1,-2,-3,-4,-5]) == 0