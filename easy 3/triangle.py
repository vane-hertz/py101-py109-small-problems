def triangle(num):
    i = 1
    while i < int(num) + 1:
        j = 0
        spaces = int(num) - i
        k = 0
        while k in range(0, spaces):
            print(' ', end='')
            k += 1
        while j < i:
            print("*", end='')
            j += 1
        print("")
        i += 1

number = input("Input number: ")
triangle(number)