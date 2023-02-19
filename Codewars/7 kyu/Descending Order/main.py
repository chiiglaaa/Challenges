def descending_order(num):
    listed_num = list(str(num))
    for i in range(len(listed_num)):
        for j in range(i+1, len(listed_num)):
            if listed_num[i] < listed_num[j]:
                listed_num[i], listed_num[j] = listed_num[j], listed_num[i]
    result = int("".join(listed_num))
    return result
