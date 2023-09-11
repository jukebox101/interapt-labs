# Display a list of words with their count

# Naah = use an input string. Ask the user for a string to
# use to collect the letter counts
my_string = input('Enter a string ==> ')
# Convert to lower-case
my_string = my_string.lower()

# Create empty dictionary. The idea is that
# this dictionary has a letter in teh string as a key
# and the count of the letters as a Value
# # You will build the dictionary in the loop below
my_dict = {}


# Iterate over characters in string
# Inside loop if dictionary does not have an entry as that
# character as key, create an entry and assign a value of 1
# else add 1 to the (existing) dictionary entry
for char in my_string:
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1

for key, value in my_dict.items():
    print(f'{key} occurs {value} times')
# print the resultant dictionary
'''
g occurs 2 times
f occurs 1 times
h occurs 1 times
e occurs 1 times
l occurs 2 times
o occurs 1 times
'''