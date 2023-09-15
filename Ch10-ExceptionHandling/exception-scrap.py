import traceback

def func_1():
    try:
        num = 15/0

    except Exception as e:
        traceback.print_exc(e)
        print(f'In func_1...{e}')


func_1()

