import datetime

class BankAccount:
    account_no: str
    __current_balance: int
    creation_date: datetime

    def __init__(self, balance, ac_no):
        self.__current_balance = balance
        self.account_no = ac_no
        self.creation_date = datetime.datetime.now()

    def deposit(self, amount: int = 0) -> str:
        if not isinstance(amount, int) and amount < 0:
            return "Enter valid amount."
        self.__current_balance += amount
        return f"{amount} credited into account {'x'*(len(self.account_no))}{self.account_no[:-5]}."

    def withdrawal(self, amount: int = 0) -> str:
        if not isinstance(amount, int) and amount < 0:
            return "Enter valid amount."
        elif amount > self.__current_balance:
            return "Not sufficient fund."
        self.__current_balance -= amount
        return f"{amount} debited from account {'x'*(len(self.account_no))}{self.account_no[:-5]}."

    def check_balance(self) -> int:
        return self.__current_balance

    def set_balance(self, amount: int):
        self.__current_balance = amount

class SavingAccount(BankAccount):
    interest_rate : int
    limit: int = 1000

    def __init__(self, interest, balance, ac_no):
        self.interest_rate = interest
        super().__init__(balance, ac_no)

    def withdrawal(self, amount: int = 0) -> str:
        balance = super().check_balance()
        if not isinstance(amount, int) and 0 > amount > self.limit:
            return "Enter valid amount."
        elif amount > balance:
            return "Not sufficient fund."
        balance -= amount
        super().set_balance(balance)
        return f"{amount} debited from account {'x'*(len(self.account_no))}{self.account_no[:-5]}."

    def check_balance(self) -> int:
        balance = super().check_balance()
        return balance + self.calc_interest()

    def calc_interest(self) -> int:
        today_date = datetime.datetime.now()
        difference = today_date - self.creation_date
        difference_in_years = (difference.days + difference.seconds // 86400) // 365
        interest = (super().check_balance() * self.interest_rate * difference_in_years) // 100
        return interest

class DepositAccount(BankAccount):
    def __init__(self, balance, ac_no):
        super().__init__(balance,ac_no)

    @staticmethod
    def calc_interest() -> int:
        return 0