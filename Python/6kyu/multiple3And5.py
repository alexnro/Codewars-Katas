def solution(number):
    aux = 3
    solution = 0
    while aux < number:
        if aux % 3 == 0:
            solution += aux
        elif aux % 5 == 0:
            solution += aux
        aux += 1
    return solution



if __name__ == "__main__":
    
    assert solution(10) == 23