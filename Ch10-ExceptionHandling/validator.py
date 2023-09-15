def enter_float_in_range( prompt, low, high ):

        user_input = input(f'{prompt} ==> ')
        if int(user_input) > high or int(user_input) < low:
            raise Exception("Input out of range")


def enter_integer_in_range( prompt, low, high ):

        user_input = input(f'{prompt} ==> ')
        if int(user_input) > high or int(user_input) < low:
            raise Exception("Input out of range")

def enter_an_integer( prompt ):
    while True:
        try:
            user_input = int(input(f'{prompt} ==> '))
            return user_input
        except ValueError:          # except Exception
            print("Value is not an int. Try again")


def enter_a_float(prompt):
    while True:
        try:
            user_input = float(input(f'{prompt} ==> '))
            return user_input
        except ValueError:          # except Exception
            print("Value is not an float. Try again")