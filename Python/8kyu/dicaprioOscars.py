def leo(oscar):
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    elif oscar != 86 and oscar < 88:
        return "When will you give Leo an Oscar?"
    elif oscar > 88:
        return "Leo got one already!"



if __name__ == "__main__":
    
    assert leo(88) =="Leo finally won the oscar! Leo is happy"