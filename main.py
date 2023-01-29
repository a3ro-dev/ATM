from utils import pin_setup, random_fact, error_or_success, banking_features



auth = pin_setup
fact = random_fact  
err_succ = error_or_success
bank = banking_features


print("Welcome to the ATM Service")
greet_fact = fact.random_Banking_fact
print(f"Fun Fact: {greet_fact}")

print("Connecting to the Gigachad Bank Of Erdia....")
print("--------------------------------------------")




class ATM:

    @staticmethod
    def menu():
        menu = """
At Gigachad Bank of Erdia, managing your finances has never been easier. With our user-friendly online banking platform, you can:
1. Securely access your account and view your balance.
    2. Open a new account and start managing your money."""

        print(menu)
        global menu_choice
        menu_choice = int(input("Enter your choice: "))
    
    @staticmethod
    def __init__():
        print(err_succ.success_or_error)

        error = err_succ.succ_err(err_succ.success_or_error)

        if error == False:

            print("Success in establishing an unsucessful connection to the Gigachad Bank Of Erdia...")
            print("Try again later")
            print("----------------------------------------------------------------------------------")

        else:

            print("Success in establishing connection to the Gigachad Bank Of Erdia...")
            print("----------------------------------------------------------------------------------")
            ATM.menu()

            if menu_choice == 1:
                usrnm = str(input("Username: "))
                paswd = int(input("Password: "))
                auth.login(username=usrnm, password=paswd)
                print("Logged in successfully")
                print(f"Balance: {bank.view_balance(username=usrnm)}")
                menu_ = f"""
Succesfully logged in At Gigachad Bank of Erdia as {usrnm},  you can:
        1. Monitor your account activity and track your spending.
            2. Easily deposit funds in your account anytime.
                3. Withdraw funds from you account anytime."""

                print(menu_)

                menu_choice_ = int(input("Enter your choice: "))
    
            elif menu_choice == 2:
                usrnm = str(input("Username: "))
                paswd = int(input("Password: "))
                auth.user_setup(username=usrnm, password=paswd)
            elif menu_choice_ == 1:
                usrnm = str(input("Username: "))
                paswd = int(input("Password: "))
                bal = bank.view_balance(username=usrnm)
                print(f"Current balance: {bal}")
                with open(f"db/user_logs/{usrnm}.txt", 'r') as log:
                    print(log.read())
            elif menu_choice_ == 2:
                print(f"Username: {usrnm}\nBalance: {bal}")
                dep_val = int(input("Deposit Amount: "))
                bank.deposit(username=usrnm, value=dep_val)
                bal_updated = bank.view_balance(username=usrnm)
                print(f"Current balance: {bal_updated}")
            elif menu_choice_ == 3:
                print(f"Username: {usrnm}\nBalance: {bal}")
                withd_val = int(input("Withdraw Amount: "))
                bank.withdraw(username=usrnm, value=withd_val)
                bal_after_withdraw = bank.view_balance(username=usrnm)
                print(f"Current balance: {bal_after_withdraw}")




ATM()