
from utils import pin_setup, random_fact, error_or_success



auth = pin_setup
fact = random_fact  
err_succ = error_or_success


print("Welcome to the ATM Service")
greet_fact = fact.random_Banking_fact
print(f"Fact: {greet_fact}")


print("Connecting to the Gigachad Bank Of Erdia....")
print("--------------------------------------------")
print(err_succ.success_or_error)
if err_succ.success_or_error == "🔴🔴🔴":
    print("Success in establishing an unsucessful connection to the Gigachad Bank Of Erdia...")
    print("Try again later")
    print("----------------------------------------------------------------------------------")
else:
    print("Success in establishing connection to the Gigachad Bank Of Erdia...")
    print("--------------------------------------------------------------------")



