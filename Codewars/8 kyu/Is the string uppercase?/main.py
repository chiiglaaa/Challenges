def is_uppercase(inp):
    if len(inp) <= 1 and inp[0].islower():
        print(inp)
        return False
    elif len(inp) > 1:
        for i in range(len(inp)):
            print(i)
            if inp[i].islower():
                return False
    return True
