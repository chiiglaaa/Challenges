def get_sum(a,b):
    if a == b:
        return a
    result = 0
    if a > b:
        for i in range(b, a+1):
            result += i
    if b > a:
        for i in range(a, b+1):
            result += i
    return result
