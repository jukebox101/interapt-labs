from datetime import datetime

class BankAccount:
    def __init__(self, acctID, acct_holder, balance):
        self._acctID = acctID
        self._acct_holder = acct_holder
        self._date_opened = datetime.now()
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

    def make_withdrawal(self, withdrawal_amount):
        if withdrawal_amount < 0:
            print(f'Withdrawl amount must exceed 0. Withdrawl amount was: {withdrawal_amount}')
        elif self._balance - withdrawal_amount < 0:
            print(f'Withdrawl of {withdrawal_amount} failed. Overdrafts are not allowed.')
        else:
            self._balance = self._balance - withdrawal_amount

    def transfer(self, transfer_amount, target_acctID):
        if self._balance - transfer_amount > 0 and self._acct_holder == target_acctID._acct_holder:
            target_acctID._balance += transfer_amount
            self._balance -= transfer_amount
        else:
            print(f'Sorry you are unable to transfer funds')
    
    def print_acct_info(self):
        print(f' Account ID: {self._acctID}\n Account Holder: {self._acct_holder}\n Date opened: {self._date_opened}\n Account Balance: {self._balance}')

    