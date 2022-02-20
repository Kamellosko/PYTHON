def power(base,power):
    result = 1
    for index in range(power):
        result = result * base
    return result
print(power(3,7))