import string
import re
# Part 1
# 'with' closes the file automatically
with open("abespeech.txt") as abe_speech:
#     # iterates through abe_speech line by line sparated by /n
#     # enumerates each line starting at 1
    for line_num, line in enumerate(abe_speech, 1):
#         # prints line number starting from 1, and the line reversed
        print(f'line {line_num} = {line[::-1]}')

# Part 2
def remove_punc(line):
    # string.punctuation: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
    for char in string.punctuation:
        line = line.replace(char, " ")
    return line

with open("smedleybutler.txt") as smedley_txt, open("bigwords.txt", 'w') as bigwords_txt:
    for line in smedley_txt:
        line = remove_punc(line)
        for word in line.split():
            if len(word) > 9:
                print(f'Word: {word}  Line: {line}')
                bigwords_txt.write(f'Word: {word}  Line: {line} \n')