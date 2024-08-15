def century(year):
    century_num = year // 100 + 1

    if year % 100 == 0:
        century_num -= 1

    suffix = century_suffix(century_num)
    return f'{century_num}{suffix}'

def century_suffix(century_num):
    last_two = century_num % 100
    last_digit = century_num % 10

    match last_two:
        case 11 | 12 | 13:
            return 'th'
        
    match last_digit:
        case 1:
            return 'st'
        case 2:
            return 'nd'
        case 3:
            return 'rd'
        case _:
            return 'th'
        
print(century(2000))         
print(century(2001))         
print(century(1965))          
print(century(256))         
print(century(5))          
print(century(10103))      
print(century(1052))        
print(century(1127))         
print(century(11201))  