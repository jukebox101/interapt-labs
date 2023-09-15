def enter_float_in_range( prompt, low, high ):

        user_input = input(f'{prompt} ==> ')
        if int(user_input) > high or int(user_input) < low:
            raise Exception("Input out of range")


def enter_integer_in_range( prompt, low, high ):

        user_input = input(f'{prompt} ==> ')
        if int(user_input) > high or int(user_input) < low:
            raise Exception("Input out of range")

def enter_an_integer( prompt ):
    user_input = input(f'{prompt} ==> ')

    

    return prompt

def enter_a_float(prompt):
    return prompt