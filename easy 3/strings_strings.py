def stringy(num):
    result = ""
    for i in range(num):
        digit = '1' if i % 2 == 0 else '0'
        result += digit

    return result

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")   