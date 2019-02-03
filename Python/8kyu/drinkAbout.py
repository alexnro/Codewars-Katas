def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"


    
if __name__ == "__main__":

    assert people_with_age_drink(13) == 'drink toddy', "Wrong result for 13"
    assert people_with_age_drink(0) =='drink toddy', "Wrong result for 0"

    assert people_with_age_drink(17) == 'drink coke'
    assert people_with_age_drink(15) == 'drink coke'
    assert people_with_age_drink(14) == 'drink coke'

    assert people_with_age_drink(20) == 'drink beer'
    assert people_with_age_drink(18) == 'drink beer'

    assert people_with_age_drink(22) == 'drink whisky'
    assert people_with_age_drink(21) == 'drink whisky'