def trim(phrase, size):
    if size >= len(phrase):
        return phrase
    result = ''
    if size <= 3:
        for i in range(size):
            result += phrase[i]
        result += "..."
        return result
    if size > 3:
        for i in range(size-3):
            result += phrase[i]
        result += "..."
        return result
