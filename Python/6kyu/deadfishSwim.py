def parse(data):
    array = list(data)
    acumulador = 0
    result = []
    for character in array:
        if character == 'i':
            acumulador += 1
        elif character == 'd':
            acumulador -= 1
        elif character == 's':
            acumulador = acumulador ** 2
        elif character == 'o':
            result.append(acumulador)
    return result



if __name__ == "__main__":
    
    assert parse("ooo") == [0,0,0]
    assert parse("ioioio") == [1,2,3]
    assert parse("idoiido") == [0,1]
    assert parse("isoisoiso") == [1,4,25]
    assert parse("codewars") == [0]