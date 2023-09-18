# 'with' closes the file automatically
with open("abespeech.txt") as abe_speech:
    for line_num, line in enumerate(abe_speech, 1):
        print(f'line {line_num} = {line[::-1]}')