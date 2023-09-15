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

def reverse_str (str1):
    str_list = list(str1)
    reversed_str = ''

    for i in str1:
        char = str_list.pop()
        reversed_str += char

    return reversed_str

# print(reverse_str("Hello World"))

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

def num_factorial (num):
    result = 1
    for i in range(1,num+1):
        result = result*i

    return result

# print(num_factorial(2))

# 6. Write a Python function to check whether a number falls within a given range.
def in_range (num, min, max):
    
    if num >= min and num <= max:
        print("Within range")
    else:
        print("Not within range")

# in_range(1, 1, 7)

# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def upper_lower (str):
    upper_count = 0
    lower_count = 0
    for char in str:
        if char != " ":
            if char.upper() == char:
                upper_count += 1
            elif char.lower() == char:
                lower_count += 1

    print(f'Number of upper case letters: {upper_count}')
    print(f'Number of lower case letters: {lower_count}')

# upper_lower("HelLo WoRld")

# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def distinct_elems (list):

    return [elem for elem in set(list)]
    
# print(distinct_elems([1,2,1,3]))

# 9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

def prime_num (num):
    if num % 2 == 1:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')

# prime_num(13)

# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def find_even_nums (num_list):

    return [num for num in num_list if num % 2 == 0 or num == 2]

# print(find_even_nums([2,3,4,5,6,2,3,4]))

# 11. Write a Python function to check whether a number is "Perfect" or not.
# According to Wikipedia : In number theory, a perfect number is a positive integer that is equal 
# to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding 
# the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number 
# that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

# def find_divisors (num):
#     divisor_list = [1]
#     for i in range(1,num+1):
#         if num % i != 1:
#             print(num/i)

# find_divisors(6)

# 12. Write a Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
# Click me to see the sample solution

# 13. Write a Python function that prints out the first n rows of Pascal's triangle.
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

# Sample Pascal's triangle :

# Pascal's triangle
# Each number is the two numbers above it added together
# Click me to see the sample solution

# 14. Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Click me to see the sample solution

# 15. Write a Python program that accepts a hyphen-separated sequence of words as input 
# and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
# Click me to see the sample solution

# 16. Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
# Click me to see the sample solution

# 18. Write a Python program to execute a string containing Python code.
# Click me to see the sample solution

# 19. Write a Python program to access a function inside a function.
# Click me to see the sample solution

# 20. Write a Python program to detect the number of local variables declared in a function.
# Sample Output:
# 3
# Click me to see the sample solution

# 21. Write a Python program that invokes a function after a specified period of time.
# Sample Output:
# Square root after specific miliseconds:
# 4.0
# 10.0
# 158.42979517754858
# Click me to see the sample solution