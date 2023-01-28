def replace_dots(str):
    result = ''
    for i in range(len(str)):
        if str[i] != '.':
            result += str[i]
        else:
            result += '-'
    return result
