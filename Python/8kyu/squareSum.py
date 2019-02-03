def square_sum(array):
    result = 0
    for number in array:
        counter = number ** 2
        result = counter + result
    return result

## Other solution
# def square_sum(numbers):
#     posicionActual = 0
#     resultado = 0
#     while posicionActual <= len(numbers) - 1:
#         numbers[posicionActual] = numbers[posicionActual] ** 2
#         resultado = resultado + numbers[posicionActual]
#         posicionActual = posicionActual + 1
#     return resultado




if __name__ == "__main__":
    
    assert square_sum([1,2]) == 5
    assert square_sum([0, 3, 4, 5]) == 50