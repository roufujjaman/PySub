class Person:
    def __init__(self, first_name: str, last_name: str, email: str, address: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address

class User(Person):
    def __init__(self, first_name: str, last_name: str, email: str, address: str, account_type = '0'):    # [0]saving, [1]current
        super().__init__(first_name, last_name, email, address)
        self.__id = None
        self.__bank = None
        self.__balance = 0
        self.account_type = int(account_type)
        self.laon_count = None
        self.transactions = {"deposit": [], "withdraw": [], "transfer": []}

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, val):
        self.__id = val
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, val):
        self.__balance = val
    
    @property
    def account_number(self):
        return "23" + f"{self.__id}".rjust(8, "0")
    
    @property
    def bank(self):
        return self.__bank
    
    @bank.setter
    def bank(self, val):
        self.__bank = val
        

    def deposit(self, amount: int, type = "deposit"):
        if not self.__bank.transaction_status:
            return "ALL TRANSECTIONS ARE FROZEN"
        
        self.balance += amount
        self.__bank.balance += amount
        self.transactions[type].append(amount)
        return f"{type.upper()} SUCCESSFUL"
        
    def withdraw(self, amount: int, type = "withdraw"):
        if not self.__bank.transaction_status:
            return "ALL TRANSECTIONS ARE FROZEN"
        elif amount > self.balance:
            return "INSUFFICIENT BALANCE (USER)"
        
        self.__balance -= amount
        self.__bank.balance -= amount
        self.transactions[type].append(amount)
        return f"{type.upper()} SUCCESSFUL"

    def transfer(self, amount: int, id: int, type = "transfer"):
        if not self.__bank.transaction_status:
            return "ALL TRANSECTIONS ARE FROZEN"
        elif amount > self.balance:
            return "INSUFFICIENT BALANCE OF USER"
        
        user = self.__bank.get_user(id)
        if isinstance(user, User):
            self.__balance -= amount
            self.transactions[type].append(amount)
            user.balance += amount
            user.transactions["deposit"].append(amount)
            return f"{type.upper()} SUCCESSFUL"
        else:
            return "ACCOUNT DOES NOT EXIST"

    def take_loan(self, amount: int):
        if not self.__bank.transaction_status:
            return "ALL TRANSECTIONS ARE FROZEN"
        if not self.__bank.loan_status:
            return "ALL LOANS ARE FROZEN BY BANK"
        
        if amount < self.__bank.balance:
            if self.laon_count > 0:
                self.__bank.balance -= amount
                self.__bank.loan_amount += amount
                self.laon_count -= 1
                self.balance += amount
                self.transactions["deposit"].append(amount)
                return "LOAN DISBURSED"
            else:
                return "LOAN AVAILED MAXIMUM NUMBER OF TIME"
        else:
            return "INSUFFICIENT BALANCE (BANK)"
    
    def user_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
    
    def __repr__(self) -> str:
        user_details = "A/C NUMBER".ljust(15) + f"- {self.account_number}\n"
        user_details += "NAME".ljust(15) + f"- {self.first_name.title()} {self.last_name.title()}\n"
        user_details += "ADDRESS".ljust(15) + f"- {self.address.title()}\n"
        user_details += "TYPE".ljust(15) + f"- {self.__bank.categories[self.account_type]}"
        return user_details