def sum_two_smallest_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    
    result = numbers[0] + numbers[1]
    return result
