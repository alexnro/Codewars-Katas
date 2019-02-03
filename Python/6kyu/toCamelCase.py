def to_camel_case(text):
    result = ''
    for character in text:
        if character == '_' or character == '-':
            text = text.replace(character, ' ')
    if (' ') in text:       
        firstSpace = text.find(' ')
        firstWord = text[:firstSpace]
        titleString = text[firstSpace:]  
        titledString = titleString.title()
        newString = firstWord + titledString
        result = result + newString.replace(' ', '')
    return result



if __name__ == "__main__":

    assert to_camel_case('') == ''
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"