def is_double_num(num):
    string_num = str(num)
    center = len(string_num) // 2
    left_num = string_num[:center]
    right_num = string_num[center:]

    return left_num == right_num

def twice(num):
    if is_double_num(num):
        return num
    else:
        return num * 2