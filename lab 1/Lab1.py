def cubick(num):
    value = 0
    for n in str(num):
        if n == "0":
            value += 1
        else:
            break

    return value
