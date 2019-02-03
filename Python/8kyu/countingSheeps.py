def count_sheeps(arrayOfSheeps):
    result = 0
    for boolean in arrayOfSheeps:
        if boolean == True:
            result += 1
    return result

## Other solution
# def count_sheeps(arrayOfSheeps):
#     posicionActual = 0
#     contador = 0
#     while posicionActual <= len(arrayOfSheeps) - 1:
#         if arrayOfSheeps[posicionActual] == True:
#             contador = contador + 1
#             posicionActual = posicionActual + 1
#         else:
#             posicionActual = posicionActual + 1
#     return contador



if __name__ == "__main__":
    
    array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]
              
    assert count_sheeps(array1) == 17