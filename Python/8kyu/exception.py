def problem(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"



if __name__ == "__main__":
    


    assert problem("hello") == "Error"
    assert problem(1) == 56