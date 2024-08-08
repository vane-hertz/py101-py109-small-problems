def center_of(string):
    mid = int(len(string) / 2)
    if int(len(string)) % 2 == 1:
        return string[mid]
    else:
        return string[mid - 1:mid + 1]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")    