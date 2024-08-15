def clean_up(string):
    result = ''

    for i, char in enumerate(string):
        if char.isalpha():
            result += char
        elif i == 0 or result[-1] != ' ':
            result += ' '
    
    return result


print(clean_up("---what's my +*& line?") == " what s my line ")
