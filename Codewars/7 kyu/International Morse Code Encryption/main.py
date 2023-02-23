#CHAR_TO_MORSE preloaded to convert characters into Morse code
def encryption(string):
    result = ''
    for i in string:
        if i.isalnum():
            result += CHAR_TO_MORSE[i] + " "
        elif i == " ":
            result += "  "
    return result.rstrip()
