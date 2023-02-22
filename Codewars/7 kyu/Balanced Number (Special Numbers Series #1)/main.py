def balanced_num(number):
    str_num = str(number)
    if len(str_num) <= 2:
        return 'Balanced'
    else:
        middle = len(str_num)//2
        if len(str_num)%2==0:
            left = str_num[:middle-1]
            right = str_num[middle+1:]
        else:
            left = str_num[:middle]
            right = str_num[middle+1:]
        resultL = 0
        resultR = 0
        
        for i in range(len(left)):
            resultL += int(left[i])
        
        for i in range(len(right)):
            resultR += int(right[i])
        
        if resultL == resultR:
            return "Balanced"
        else:
            return "Not Balanced"
