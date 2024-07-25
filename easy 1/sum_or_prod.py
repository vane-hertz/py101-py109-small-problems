number = int(input("Please enter an integer greater than 0: "))
sum_or_prod = input("Enter \"s\" to compute the sum, or \"p\" to compute the product. ")
if (sum_or_prod == "s"):
    sum = 0
    num = number
    while (number > 0):
        sum += number
        number -= 1
    print(f"The sum of the integers between 1 and {num} is {sum}.")
elif (sum_or_prod == "p"):
    product = 1
    num = number
    while (number > 0):
        product *= number
        number -= 1
    print(f"The product of the integers between 1 and {num} is {product}.")