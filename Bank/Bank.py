from Person import User
class Bank:
    def __init__(self, name, location, branch, initial_amount = 0):
        self.name = name
        self.location = location
        self.branch = branch
        self.admin = None
        self.__balance = initial_amount
        self.__users = {}
        self.user_limit = 99999999          # 8

        self.transaction_status = True      # True - Unfrozen, False - Frozen 
        self.loan_status = True             # True - Unfrozen, False - Frozen
        self.loan_amount = 0
        self.loan_numberlimit = 2

        self.categories = ["Savings", "Current"]
        self.curr_users = 0

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        self.__balance = amount
        
    @property
    def users(self):
        return self.__users
    
    def add_user(self, user):
        if self.curr_users < self.user_limit:
            self.__users[user.id] = user
            self.curr_users += 1
            return True
        else:
            return False
        

    def get_user(self, id):
        if id in self.__users:
            return self.__users[id]
        else:
            return None
        
    def gen_id(self):                           # generate id
        return self.curr_users + 1
    

class Admin:
    def __init__(self,bank: Bank, id = 1, password = "1234"):
        bank.admin = self
        
        self.bank = bank
        self.id = id
        self.password = password
    
    def create_acocunt(self, user: User):
        if self.bank.curr_users <= self.bank.user_limit:
            if isinstance(user, User):
                user.bank = self.bank
                user.id =  self.bank.gen_id()
                user.laon_count = self.bank.loan_numberlimit
                if self.bank.add_user(user):
                    return "ACCOUNT CREATED"
                else:
                    return "MAXIMUM USER REACHED"
            else:
                return "INVALID USER"
    
    def delet_acount(self, id: int):
        if id not in self.bank.users:
            return "ACCOUNT DOES NOT EXIST"

        del self.bank.users[id]
        return "ACCOUNT DELETION SUCCESSFUL"
    
    def view_accounts(self):
        users = self.bank.users
        if users:
            users_list = ""
            for i, user in enumerate(users, 1):
                users_list += f"{i}\n"
                users_list += f"{users[user]}\n\n"
            return users_list
        else:
            return "NO USER"
    
    def curr_balance(self):
        return f"CURRENT BALANCE: {self.bank.balance}"

    def curr_loanamount(self):
        return f"CURRENT LOAN AMOUNT: {self.bank.loan_amount}"
    
    def freez_loan(self):
        self.bank.loan_status = False
        return "ALL LOANS ARE FROZEN"
    
    def unfreez_loan(self):
        self.bank.loan_status = True
        return "ALL LOAN ARE UNFROZEN"

    def freez_transaction(self):
        self.bank.transaction_status = False
        return "ALL TRANSACTIONS ARE FROZEN"
    
    def unfreez_transaction(self):
        self.bank.transaction_status = True
        return "ALL TRANSACTIONS ARE UNFROZEN"