import sys

# Part 1
my_name = input(f'Enter your name ==> ')
print(f"my_name = '{my_name}'")
print(f'I am {my_name}')
print(f'I am\n {my_name: ^20}\nand I code for a living')

# Part 2
arg1 = float(sys.argv[1])
arg2 = float(sys.argv[2])
print(f'Sum of {arg1} and {arg2} is {arg1 + arg2}')