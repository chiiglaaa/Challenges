import math

def is_square(n):
    if n < 0:
        return False
    answer = math.sqrt(n)
    if answer != int(answer):
        return False
    return True
