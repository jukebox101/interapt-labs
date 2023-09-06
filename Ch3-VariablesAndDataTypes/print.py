# aVar = 100
# bVar = 200

# print(aVar + bVar)
# print(f'first variable: {aVar}, second variable: {bVar}')

letter_a = "A"
three_spaces = "   "
print(f'{letter_a: ^38}')
print(f'{letter_a: >17}{three_spaces}{letter_a:<17}')
print(f'{letter_a: >16}',end="" )
print(f'{letter_a}{letter_a}{letter_a}{letter_a}{letter_a}{letter_a:<15}' )
print(f'{letter_a: >15}{three_spaces:>7}{letter_a:<15}')
print(f'{letter_a: >14}{three_spaces:>9}{letter_a:<14}')