def is_uppercase(inp):
    if len(inp) <= 1 and inp[0].islower():
        return False
    elif len(inp) > 1:
        for i in range(len(inp)):
            if inp[i].islower():
                return False
    return True
