def multisum(num):
    sum = 0
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)