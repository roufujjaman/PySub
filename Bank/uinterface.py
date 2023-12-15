UI = (50, "-", ".")

def ui_notify(val: str):
    val = str(val)
    return val.rjust(UI[0], UI[2])

def ui_label(val: any):
    return str(val).ljust(UI[0], UI[2])

def ui_center(val: str):
    return val.center(UI[0], UI[1])

def ui_show_admin():
    print("ADMIN".center(UI[0], UI[1]))
    print("[1] CREATE ACCOUNT")
    print("[2] DELETE ACCOUNT")
    print("[3] VIEW ALL ACCOUNTS")
    print("[4] CHECK CURRENT BALANCE")
    print("[5] CHECK CURRENT LOAN AMOUNT")
    print("[6] FREEZE")
    print("[7] UNFREEZE")
    print("[8] EXIT")
    input_val = int(input("(ADMIN) INSERT SELECTION: "))
    return input_val

def ui_input_user(person: str):
    fname = input(f"({person.upper()}) INSERT FIRST NAME: ")
    lname = input(f"({person.upper()}) INSERT LAST NAME: ")
    email = input(f"({person.upper()}) INSERT EMAIL: ")
    address = input(f"({person.upper()}) INSERT ADDRESS: ")
    print("[0 = Savings, 1 = CURRENT]")
    account_type = input(f"({person.upper()}) INSERT A/C TYPE[0, 1]: ")
    if account_type in ['0', '1']:
        return [fname, lname, email, address, account_type]
    else:
        return [fname, lname, email, address]
    
def ui_input_amount(type: str, person: str):
    try:
        amount = int(input(f"({person.upper()}) INSERT {type} AMOUNT: "))
        return amount
    except ValueError:
        return 0

def ui_input_accountnumber(person: str):
    account_number = input(f"({person.upper()}) INSERT A/C NUMBER: ")
    if len(account_number) == 10 and account_number.isnumeric():
        id = int(account_number[2:])
        return id
    else:
        return None

def ui_show_user(person: str):
    print(f"USER|{person}".center(UI[0], UI[1]))
    print("[1] DEPOSIT")
    print("[2] WITHDRAW")
    print("[3] TRANSFER")
    print("[4] BALANCE")
    print("[5] TRANSECTIONS")
    print("[6] TAKE LOAN")
    print("[7] EXIT")
    input_val = int(input("(USER) INSERT SELECTION: "))
    return input_val