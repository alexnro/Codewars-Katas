from math import sqrt

def is_square(n):  
    if n >=0:
        return (sqrt(n) *10) % 10 == 0
    else:
        return False



if __name__ == "__main__":
        
    assert is_square(-1) == False
    assert is_square( 0) == True 
    assert is_square( 3) == False
    assert is_square( 4) == True 
    assert is_square(25) == True
    assert is_square(26) == False