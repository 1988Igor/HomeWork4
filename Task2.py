# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Enter a number: '))
user_number = number
divider = 2
lst = []
while divider <= number:
    if number % divider == 0:
        lst.append(divider)
        number = number // divider
        divider = 2
    else:
        divider += 1
print(f'Simple multipliers of number {user_number} is : {lst}')