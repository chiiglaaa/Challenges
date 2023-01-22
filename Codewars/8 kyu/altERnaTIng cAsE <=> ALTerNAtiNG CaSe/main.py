def to_alternating_case(string):
    low = 'abcdefghijklmnopqrstuvwxyz'
    high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    low = list(low)
    high = list(high)

    ans = []
    for i in string:
        if i in low:
            ans.append(i.upper())
        else:
            ans.append(i.lower())

    return "".join(ans)
