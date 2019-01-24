def duplicate_encode(word):
    word = word.lower()
    result = ""
    for characters in word:
        if word.count(characters) > 1:
            result = result + ')'
        else:
            result = result + '('
    return result