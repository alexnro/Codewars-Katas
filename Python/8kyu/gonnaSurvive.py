def hero(bullets, dragons):
    if bullets >= dragons*2:
        return True
    else:
        return False


if __name__ == "__main__":
    
    assert hero(10, 5) == True
    assert hero(7, 4) == False
    assert hero(4, 5) == False
    assert hero(100, 40) == True
    assert hero(1500, 751) == False
    assert hero(0, 1) == False