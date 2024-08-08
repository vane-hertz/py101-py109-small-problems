def penultimate(string):
    li = string.split(" ")
    return li[len(li) - 2]

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")