def utf16_value(string):
    sum = 0
    for char in string:
        sum += ord(char)
    return sum