#Write a program that accepts numeric inputs and adds them to a set.
#Hit <enter> when done
#After making entries, print the largest, smallest, sum, and average of all elements

user_input = input('Enter a number you want in your set, or press Enter to exit ==> ')
user_set = set()

while user_input != '':
    user_set.add(int(user_input))
    user_input = input('Enter a number you want in your set, or press Enter to exit ==> ')


print(f'{user_set}')
print(f'Max Value in Set: {max(user_set)}')
print(f'Min Value in Set: {min(user_set)}')
print(f'Sum of All Values in Set: {sum(user_set)}')
print(f'Average of All Values in Set: {sum(user_set) / len(user_set)}')