import random

ch1 = "🔴🔴🔴"
ch2 = "🟢🟢🟢"
choice = [ch1, ch2]

success_or_error = random.choice(choice)
def succ_err(success_or_error):
    if success_or_error == "🔴🔴🔴":
        return False
    if success_or_error == "🟢🟢🟢":
        return True


        