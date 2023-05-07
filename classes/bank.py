class Account:
    bank_name="Equity"

    def __init__(self,account_name,account_number,account_balance):
        self.account_name=account_name
        self.account_balance=account_balance
        self.account_number=account_number


    def withdrawal(self):
        self.withdraw=3678
        if self.account_balance>=self.withdraw:
            self.account_balance2=self.account_balance-self.withdraw
        return f"The account balance of account name {self.account_name} of account number {self.account_number} is {self.account_balance2}"

    def deposit(self):
        self.deposit_money=34567
        self.account_balance2=self.account_balance+self.deposit_money
        return f"The account balance of account name {self.account_name} is {self.account_balance2}"

    def send_money(self):
        self.money_sent=3456
        if self.account_balance>=self.money_sent:
            self.account_balance2=self.account_balance-self.money_sent
        return f"{self.account_balance2}"

    
