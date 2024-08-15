def crunch(string):
    i = 0
    crunched_text = ""
    while i < len(string):
        if i == len(string) - 1 or string[i] != string[i + 1]:
            crunched_text += string[i]

        i += 1
    return crunched_text

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')