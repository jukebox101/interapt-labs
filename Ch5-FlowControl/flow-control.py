import sys;

target = 45
guesses = 5
start_answer = input("Wanna play a number game? (y or n) ==> ")

if start_answer == 'y':
    user_guess = input('Enter a number between 1 and 100 ==> ')
    for guess in range(guesses):    
        if int(user_guess) == target:
            print('Great job! You guessed correctly')
            sys.exit(0)
        else:
            guesses -= 1
            print('No dice, try again')        
            user_guess = input('Enter a number between 1 and 100 ==> ')
elif start_answer == 'n':
    sys.exit(0)