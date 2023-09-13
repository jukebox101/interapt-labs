# 1. Write a Python function to find the maximum of three numbers.
def find_max_three (num1, num2, num3):
    max = num1

    if max < num2:
        max = num2
    if max < num3:
        max = num3

    return max

# print(find_max_three(23, 54, 11))

# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def list_sum (num_list):
    sum = 0

    for num in num_list:
        sum += num

    return sum

# print(list_sum([12,23,34]))

# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def list_multiply (num_list):
    product = 1

    for num in num_list:
        product = product * num

    return product

# print(list_multiply([1,2,3]))

# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse_str(str1):
    str_list = list(str1)
    reversed_str = ''

    for i in str1:
        char = str_list.pop()
        reversed_str += char

    return reversed_str

# print(reverse_str("Hello World"))

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

def num_factorial(num):
    result = 1
    for i in range(1,num+1):
        result = result*i

    return result

# print(num_factorial(2))

