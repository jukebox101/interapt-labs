class BankAccount:
    def __init__(self, acctID, acct_holder, date_opened, balance):
        self._acctID = acctID
        self._acct_holder = acct_holder
        self._date_opened = date_opened
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print(f'{new_balance} is less than 0. Overdrafts are not allowed.')

    def make_deposit(self, deposit_amount):
        if deposit_amount < 0:
            print(f'Deposit amount must exceed 0. Deposit amount was: {deposit_amount}')
        else:
            self._balance = self._balance + deposit_amount

    def make_withdrawl(self, withdrawal_amount):
        if withdrawal_amount < 0:
            print(f'Withdrawl amount must exceed 0. Withdrawl amount was: {withdrawal_amount}')
        elif self._balance - withdrawal_amount < 0:
            print(f'Withdrawl of {withdrawal_amount} failed. Overdrafts are not allowed.')
        else:
            self._balance = self._balance - withdrawal_amount

    