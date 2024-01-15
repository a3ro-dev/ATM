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
    """
    Represents an ATM service that allows users to open a new account or access an existing account.
    Users can view their account balance, monitor their account activity, deposit funds, and withdraw funds.
    """

    def __init__(self):
        """
        Initializes the ATM class and establishes a connection to the bank.
        If the connection is successful, it calls the `run()` method.
        """
        error = err_succ.succ_err(err_succ.success_or_error)
        if error == False:
            print("Success in establishing a connection to the Gigachad Bank Of Erdia...")
            self.run()
        else:
            print("Unsuccessful in establishing a connection to the Gigachad Bank Of Erdia...")
            print("Try again later")
            print("----------------------------------------------------------------------------------")

    def run(self):
        """
        Displays the main menu and handles user input to either open a new account or access an existing account.
        """
        self.menu()
        menu_choice = int(input("Enter your choice: "))
        if menu_choice == 2:
            self.handle_new_account()
        if menu_choice == 1:
            self.handle_existing_account()

    @staticmethod
    def menu():
        """
        Displays the menu options for the ATM service.
        """
        menu = """
        At Gigachad Bank of Erdia, managing your finances has never been easier. With our user-friendly online banking platform, you can:
        1. Securely access your account and view your balance.
        2. Open a new account and start managing your money."""
        print(menu)

    def handle_new_account(self):
        """
        Prompts the user to enter a username and password to create a new account.
        """
        usrnm = str(input("Username: "))
        paswd = int(input("Password: "))  # Convert password to integer
        auth.user_setup(username=usrnm, password=paswd)

    def handle_existing_account(self):
        """
        Prompts the user to enter a username and password to access an existing account.
        If successful, it displays the account balance and calls the `handle_account_menu()` method.
        """
        usrnm = str(input("Username: "))
        paswd = int(input("Password: "))  # Convert password to integer
        auth.login(username=usrnm, password=paswd)
        print("Logged in successfully")
        print(f"Balance: {bank.view_balance(username=usrnm)}")
        self.handle_account_menu(usrnm)

    def handle_account_menu(self, usrnm):
        """
        Displays the account menu options for an existing account and handles user input to perform different actions.
        """
        menu_ = f"""
        Succesfully logged in At Gigachad Bank of Erdia as {usrnm},  you can:
        1. Monitor your account activity and track your spending.
        2. Easily deposit funds in your account anytime.
        3. Withdraw funds from you account anytime."""
        print(menu_)
        menu_choice = int(input("Enter your choice: "))
        if menu_choice == 1:
            self.handle_account_activity(usrnm)
        if menu_choice == 2:
            self.handle_deposit(usrnm)
        if menu_choice == 3:
            self.handle_withdraw(usrnm)

    def handle_account_activity(self, usrnm):
        """
        Displays the current account balance and the account activity log.
        """
        bal = bank.view_balance(username=usrnm)
        print(f"Current balance: {bal}")
        with open(f"db/user_logs/{usrnm}.txt", 'r') as log:
            print(log.read())

    def handle_deposit(self, usrnm):
        """
        Displays the current account balance and prompts the user to enter a deposit amount.
        Updates the account balance after the deposit.
        """
        bal = bank.view_balance(username=usrnm)
        print(f"Username: {usrnm}\nBalance: {bal}")
        dep_val = int(input("Deposit Amount: "))
        bank.deposit(username=usrnm, value=dep_val)
        bal_updated = bank.view_balance(username=usrnm)
        print(f"Current balance: {bal_updated}")

    def handle_withdraw(self, usrnm):
        """
        Displays the current account balance and prompts the user to enter a withdrawal amount.
        Checks if the withdrawal amount is valid and updates the account balance accordingly.
        """
        bal = bank.view_balance(username=usrnm)
        print(f"Username: {usrnm}\nBalance: {bal}")
        wit_val = int(input("Withdraw Amount: "))
        if wit_val > bal:
            print("You don't have enough balance.")
        elif wit_val == bal:
            print("You'll end up with 0 balance.")
            sure = str(input("Are you sure you want to empty you bank account?"))
            if sure.lower() in ["no", "n", "nope"]:
                raise ValueError("Withdrawal cancelled by user")
            else:
                bank.withdraw(username=usrnm, value=wit_val)
                bal_updated = bank.view_balance(username=usrnm)
                print(f"Balance: {bal_updated}")

ATM()