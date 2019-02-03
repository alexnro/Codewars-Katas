def duplicate_encode(word):
    word = word.lower()
    result = ""
    for characters in word:
        if word.count(characters) > 1:
            result = result + ')'
        else:
            result = result + '('
    return result



if __name__ == "__main__":
    
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("