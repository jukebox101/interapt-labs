import sys;

# Part 1
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
            print(f'No dice, try again! You have {guesses} guesses left!')        
            user_guess = input('Enter a number between 1 and 100 ==> ')
elif start_answer == 'n':
    sys.exit(0)

# Part 2
user_input = input('Enter:/n    C to create,/n  R to read,/n    U to update,/n  D to delete or/n    Q to quit ==> ') 
while user_input.upper() != 'Q' :
    if user_input.upper() == 'C':
        print("Calling CREATE routine...")
        user_input = input('Enter:/n    C to create,/n  R to read,/n    U to update,/n  D to delete or/n    Q to quit ==> ')
    elif user_input.upper() == 'R':
        print("Calling READ routine...")
        user_input = input('Enter:/n    C to create,/n  R to read,/n    U to update,/n  D to delete or/n    Q to quit ==> ')
    elif user_input.upper() == 'U':
        print("Calling UPDATE routine...")
        user_input = input('Enter:/n    C to create,/n  R to read,/n    U to update,/n  D to delete or/n    Q to quit ==> ')
    elif user_input.upper() == 'D':
        print("Calling DELETE routine...")
        user_input = input('Enter:/n    C to create,/n  R to read,/n    U to update,/n  D to delete or/n    Q to quit ==> ')
print("Exiting the program...")