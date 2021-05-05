def spiralize(size, n=1):
    n = input("Enter your value: ")
    cnt = 0
    inc = 2
    return_value = 0

    while n <= size ** 2:
        return_value += n
        n += inc
        cnt += 1
        if cnt == 4:
            inc += 2
            cnt = 0

    return_value = n
    return return_value
