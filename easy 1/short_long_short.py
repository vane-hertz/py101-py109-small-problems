def short_long_short(str1, str2):
    big_string = ""
    short_string = ""
    if len(str1) > len(str2):
        big_string = str1
        short_string = str2
    elif len(str2) > len(str1):
        big_string = str2
        short_string = str1
    return short_string + big_string + short_string

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
