from Bank import Bank, Admin
from Person import User
from uinterface import UI, ui_show_user, ui_show_admin, ui_input_user
from uinterface import ui_notify, ui_center, ui_label, ui_input_amount
from uinterface import ui_input_accountnumber
def main():
    bank = Bank("AB", "UT", "BR", 1000000)
    admin = Admin(bank)

    while True:
        print("[1] ADMIN")
        print("[2] USER")
        print("[3] EXIT")
        try:
            input_val = int(input("INSERT SELECTION: "))
        except ValueError:
            print(ui_notify("INVALID INPUT VALUE"))
            continue

        if input_val == 1:
            input_id = input("(ADMIN) INSERT ID: ")
            input_password = input("(ADMIN) INSERT PASSWORD: ")
            if not input_id.isnumeric():
                print(ui_notify("INVALID ID"))
                continue
            elif input_password != admin.password:
                print(ui_notify("INVALID PASSWORD"))
                continue
                
            id = int(input_id)
            password = input_password

            if id == admin.id and password == admin.password:
                while True:
                    try:
                        val = ui_show_admin()
                    except ValueError:
                        print(ui_notify("INVALID INPUT VALUE"))
                        continue

                    if val == 1:
                        print(ui_center("ADMIN|CREATE USER"))
                        user_info = ui_input_user("ADMIN")
                        user = User(*user_info)
                        create_msg = admin.create_acocunt(user)
                        print(ui_notify(create_msg))
                    elif val == 2:
                        print(ui_center("ADMIN|DELETE USER"))
                        id = ui_input_accountnumber("ADMIN")      # 23 00000000   - 10 digit
                        delete_msg = admin.delet_acount(id)     # 2300000001    - 10 digit
                        print(ui_notify(delete_msg))
                    elif val == 3:
                        print(ui_center("ADMIN|ALL USERS"))
                        users_msg = admin.view_accounts()
                        print(users_msg)
                    elif val == 4:
                        print(ui_center("ADMIN|CURRENT BALANCE"))
                        balance_msg = admin.curr_balance()
                        print(ui_notify(balance_msg))
                    elif val == 5:
                        print(ui_center("ADMIN|TOAL LOAN AMOUNT"))
                        loanamount_msg = admin.curr_loanamount()
                        print(ui_notify(loanamount_msg))
                    elif val == 6:
                        print(ui_center("ADMIN|FREEZ"))
                        print("[1] LOAN FACILITY")
                        print("[2] ALL TRANSECTIONS")
                        
                        val_admin = input("(ADMIN) INSERT SELECTION: ")
                        if int(val_admin) == 1:
                            freez_msg = admin.freez_loan()
                            print(ui_notify(freez_msg))
                        elif int(val_admin) == 2:
                            freez_msg = admin.freez_transaction()
                            print(ui_notify(freez_msg))
                        else:
                            print(ui_notify("INVALID INPUT"))
                    elif val == 7:
                        print(ui_center("ADMIN|UNFREEZ"))
                        print("[1] LOAN FACILITY")
                        print("[2] ALL TRANSECTIONS")
                        
                        val_admin = input("(ADMIN) INSERT SELECTION: ")
                        if int(val_admin) == 1:
                            freez_msg = admin.unfreez_loan()
                            print(ui_notify(freez_msg))
                        elif int(val_admin) == 2:
                            freez_msg = admin.unfreez_transaction()
                            print(ui_notify(freez_msg))
                        else:
                            print(ui_notify("INVALID INPUT"))
                    elif val == 8:
                        break
                    else:
                        print(ui_notify("INVALID INPUT"))                
        elif input_val == 2:
            print("[1] CREATE ACCOUNT")
            print("[2] EXISTING USER")
            try:
                val = int(input("INSERT SELECTION: "))
            except ValueError:
                print(ui_notify("INVALID INPUT VALUE"))
                continue

            if val == 1:
                print(ui_center("USER|CREATE USER"))
                user_info = ui_input_user("USER")
                user = User(*user_info)
                create_msg = admin.create_acocunt(user)
                print(ui_notify(create_msg))
            elif val == 2:
                id = ui_input_accountnumber("USER")
                user = bank.get_user(id)
                if not isinstance(user, User):
                    print(ui_notify("ACCOUNT DOES NOT EXIST"))
                    continue

                while True:
                    try:
                        val_user = ui_show_user(user.user_name())
                    except ValueError:
                        print(ui_notify("INVALID INPUT VALUE"))
                        continue
                    
                    if val_user == 1:
                        print(ui_center("USER|DEPOSIT"))
                        amount = ui_input_amount("DEPOSIT", "USER")
                        if amount > 0:
                            deposit_msg = user.deposit(amount)
                            print(ui_notify(deposit_msg))
                        else:
                            print(ui_notify("INVALID AMOUNT OR CHARACTER"))
                    elif val_user == 2:
                        print(ui_center("USER|WITHDRAW"))
                        amount = ui_input_amount("WITHDRAW", "USER")
                        if amount > 0:
                            withdraw_msg = user.withdraw(amount)
                            print(ui_notify(withdraw_msg))
                        else:
                            print(ui_notify("INVALID AMOUNT OR CHARACTER"))
                    elif val_user == 3:
                        print(ui_center("USER|TRANSFER"))
                        amount = ui_input_amount("TRANSFER", "USER")
                        if amount > 0:
                            id = ui_input_accountnumber("USER")
                            transfer_msg = user.transfer(amount, id)
                            print(ui_notify(transfer_msg))
                        else:
                            print(ui_notify("INVALID AMOUNT OR CHARACTER"))
                    elif val_user == 4:
                        print(ui_center("USER|BALANCE"))
                        print(ui_notify(user.balance))
                    elif val_user == 5:
                        print(ui_center("USER|TRANSACTIONS"))
                        for type, amounts in user.transactions.items():
                            print(ui_label(type.upper()))
                            if amounts:
                                for i, amount in enumerate(amounts, 1):
                                    print(i, f"- {amount}")
                            else:
                                print("NO TRANSACTION")
                    elif val_user == 6:
                        print(ui_center("USER|TAKE LOAN"))
                        amount = ui_input_amount("LOAN", "USER")
                        if amount > 0:
                            loan_msg = user.take_loan(amount)
                            print(ui_notify(loan_msg))
                        else:
                            print(ui_notify("INVALID AMOUNT/CHARACTER"))
                    elif val_user == 7:
                        break
                    else:
                        print(ui_notify("INVALID INPUT VALUE"))
            else:
                print(ui_notify("INVALID INPUT VALUE"))
        elif input_val == 3:
            break
        else:
            print(ui_notify("INVALID INPUT VALUE"))

if __name__ == "__main__":
    main()