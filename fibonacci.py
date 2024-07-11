def calculate (n):
    fib_list = [0,1]
    if  n <= len(fib_list):
        return fib_list[:n]
    else:
        x=2
        while x < n:
            fib = fib_list[x-2] + fib_list[x-1]
            fib_list.append(fib)
            x += 1

    return fib_list    