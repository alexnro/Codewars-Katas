def repeater(string, n):
    return string * n



if __name__ == "__main__":
        
    assert repeater('a', 5) == 'aaaaa'
    assert repeater('Na', 16) == 'NaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNa'
    assert repeater('Wub ', 6) == 'Wub Wub Wub Wub Wub Wub '