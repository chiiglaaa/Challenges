def encode(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_str = str(key)
    result = []
    j = 0
    for i in range(len(message)):
        char = message[i]
        if j == len(key_str):
            j = 0
        cipher = int(key_str[j])
        j += 1
        char_idx = alphabet.index(char) + 1
        result.append(cipher + char_idx)
    return result

