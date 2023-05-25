class Account:
    bank_name="Equity"

    def __init__(self,account_name,account_number,account_balance,deposits,withdrawals,loan_balance):
        self.account_name=account_name
        self.account_balance=account_balance
        self.account_number=account_number
        self.deposits=[]
        self.withdrawals=[]
        self.loan_balance=0


    def withdrawal(self):
        self.withdraw=3678
        if self.account_balance>=self.withdraw:
            self.account_balance2=self.account_balance-self.withdraw
        return f"The account balance of account name {self.account_name} of account number {self.account_number} is {self.account_balance2}"


        self.withdrawals.append({"amount":amount,"narration":"withdrawal"})
        return f "withrawal of {amount} successful"


    def deposit(self):
        self.deposit_money=34567
        self.account_balance2=self.account_balance+self.deposit_money
        return f"The account balance of account name {self.account_name} is {self.account_balance2}"

# Update the deposit method to append each withdrawal transaction to the deposits list. Each transaction should be in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }
        self.deposits.append({"amount":amount,"narration":"deposit"})
        return f "Deposit of {amount} successful"

    def send_money(self):
        self.money_sent=3456
        if self.account_balance>=self.money_sent:
            self.account_balance2=self.account_balance-self.money_sent
        return f"{self.account_balance2}"


# Add a method check_balance which returns the account’s balance
    def check_balance(self):
        self.amount_deposited=3000
        self.amount_withdrawed=1000
        self.account_balance=self.deposits*self.amount_deposited-self.withdrawals*self.amount_withdrawed
        return self.account_balance


# Add a new method  print_statement which combines both deposits and withdrawals
#  into one list and, using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500
    def print_statement(self):
        transactions=self.withdrawals+self.deposits
        for transaction in transactions:
            print(f" {transaction["narration"]}-{transaction["amount"]}")



# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
    def borrow_loan(self):
        self.sum_deposits=self.deposits*self.amount_deposited
        self.loan_requested=8000
        if self.loan_balance=0:
            return (f"customer can borrow")
        elif self.loan_requested>100 and 1/3*self.sum_deposits:
            return(f"customer can borrow")
        elif self.deposits>=10:
            return (f"customer can borrow")
        print self.loan_balance+=self.loan_requested

# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
    def repay_loan(self):
        self.loan_repay=4000
        print(f"{self.loan_balance}-{self.loan_repay} is the 
        current loan balance and the current account balance is
         {self.loan_repay}-{self.loan_balance}+{self.account_balance}")

# Add a transfer method which accepts two attributes (amount and instance of another account). 
# If the amount is less than the current instances balance, the method transfers the requested 
# amount from the current account to the passed account. The transfer is accomplished 
# by reducing the current account balance and depositing the requested amount to the passed account.
    def transfer(self, amount, destination_account):
        if self.amount <= sum(self.deposits):
            self.withdrawal(amount)
            destination_account.deposit(amount)
            return "Transfer successful."
        else:
            return "Insufficient funds for transfer."


# 







    
