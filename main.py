from utils import pin_setup, random_fact, error_or_success, banking_features



auth = pin_setup
fact = random_fact  
err_succ = error_or_success
bank = banking_features


print("Welcome to the ATM Service")
greet_fact = fact.random_Banking_fact
print(f"Fact: {greet_fact}")

print("Connecting to the Gigachad Bank Of Erdia....")
print("--------------------------------------------")




class ATM:

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

            menu = """
At Gigachad Bank of Erdia, managing your finances has never been easier. With our user-friendly online banking platform, you can:
1. Securely access your account and view your balance.
    2. Open a new account and start managing your money.
        3. Monitor your account activity and track your spending.
            4. Easily withdraw funds from your account at any time."""

            print(menu)

            menu_choice = int(input("Enter your choice: "))
            if menu_choice == 1:
                usrnm = str(input("Username: "))
                paswd = int(input("Password: "))
                auth.login(username=usrnm, password=paswd)
            elif menu_choice == 2:
                usrnm = str(input("Username: "))
                paswd = int(input("Password: "))
                auth.user_setup(username=usrnm, password=paswd)
            elif menu_choice == 3:
                usrnm = str(input("Username: "))
                paswd = int(input("Password: "))
                bal = bank.view_balance(username=usrnm)
                with open(f"db/user_logs/{usrnm}.txt", 'r') as log:
                    print(log.read())
            



                ATM()