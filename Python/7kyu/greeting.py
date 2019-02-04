class Person():
    
    def __init__(self, my_name):
        self.name = my_name
    
    def greet(self, your_name):
        return "Hello %s, my name is %s" % (your_name, self.name)



if __name__ == "__main__":
    
    jack = Person("Jack")
    jill = Person("Jill")

    assert jack.greet("Jill") == "Hello Jill, my name is Jack"
    assert jack.greet("Mary") == "Hello Mary, my name is Jack"

    assert jill.greet("Jack") == "Hello Jack, my name is Jill"
    assert jill.name == 'Jill'