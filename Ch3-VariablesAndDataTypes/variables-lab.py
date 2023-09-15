# Part 1

# letter_a = "A"
# three_spaces = "   "
# print(f'{letter_a: ^38}')
# print(f'{letter_a: >17}{three_spaces}{letter_a:<17}')
# print(f'{letter_a: >16}',end="" )
# print(f'{letter_a}{letter_a}{letter_a}{letter_a}{letter_a}{letter_a:<15}' )
# print(f'{letter_a: >15}{three_spaces:>7}{letter_a:<15}')
# print(f'{letter_a: >14}{three_spaces:>9}{letter_a:<14}')

# # Part 2
# num1 = 100
# num2 = 3.14159
# print(f'100 multiplied by 3.14159 = {num1*num2}')
# print(f'The type of 100 is {type(num1)}')
# print(f'The type of 3.14159 is {type(num2)}')
# print(f'The object identifier of 100 is {id(num1)}')
# print(f'The object identifier of 3.14159 is {id(num2)}')

# Part 3
string1 = "Hello"
string2 = "Hello"

if string1 == string2:
    print(f'{string1} is the same as {string2}')
else:
    print(f'{string1} is not the same as {string2}')

print(f'Before the arithmetic: string1 = {id(string1)} and string2 = {id(string2)}')

string1 = string1 + " There"
string2 = string2 + " There"


if string1 == string2:
    print(f'{string1} is the same as {string2}')
else:
    print(f'{string1} is not the same as {string2}')

print(f'After the arithmetic: string1 = {id(string1)} and string2 = {id(string2)}')

num1 = 10
num2 = 10.0

print(f'Before the arithmetic: num1 = {id(num1)} and num2 = {id(num2)}')

if num1 == num2:
    print(f'{num1} is the same as {num2}')
else:
    print(f'{num1} is not the same as {num2}')

num1 = num1 + 100
num2 = num2 - 5

print(f'After the arithmetic: num1 = {id(num1)} and num2 = {id(num2)}')

