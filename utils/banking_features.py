import sqlite3
import datetime

def deposit(username, value):
    # Connect to the database
    conn = sqlite3.connect('db/atm.db')
    c = conn.cursor()

    # Check if the user's table exists in the database
    c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{username}'")
    table_exists = c.fetchone()

    # If the table doesn't exist, create it
    if table_exists is None:
        c.execute(f"CREATE TABLE {username} (balance INTEGER)")

    # Deposit the value into the user's balance
    c.execute(f"UPDATE {username} SET balance = balance + {value}")
    conn.commit()

    # Log the transaction
    with open(f"db/user_logs/{username}.txt", "a") as log:
        log.write(f"Deposited {value} at {datetime.datetime.now()}\n")

    # Close the connection to the database
    conn.close()

def withdraw(username, value):
    # Connect to the database
    conn = sqlite3.connect('db/atm.db')
    c = conn.cursor()

    # Check if the user's table exists in the database
    c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{username}'")
    table_exists = c.fetchone()

    # If the table doesn't exist, create it
    if table_exists is None:
        c.execute(f"CREATE TABLE {username} (balance INTEGER)")

    # Withdraw the value from the user's balance
    c.execute(f"UPDATE {username} SET balance = balance - {value}")
    conn.commit()

    # Log the transaction
    with open(f"db/user_logs/{username}.txt", "a") as log:
        log.write(f"Withdrew {value} at {datetime.datetime.now()}\n")

    # Close the connection to the database
    conn.close()

def view_balance(username):
    # Connect to the database
    conn = sqlite3.connect('db/atm.db')
    c = conn.cursor()

    # Check if the user's table exists in the database
    c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{username}'")
    table_exists = c.fetchone()

    # If the table doesn't exist, create it
    if table_exists is None:
        c.execute(f"CREATE TABLE {username} (balance INTEGER)")

    # Retrieve the user's balance
    c.execute(f"SELECT balance FROM {username}")
    balance = c.fetchone()[0]

    # Close the connection to the database
    conn.close()

    return balance
