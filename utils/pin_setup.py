import sqlite3
import hashlib

def create_table(username: str) -> None:
    # connect to the database
    conn = sqlite3.connect('db/atm.db')
    cursor = conn.cursor()
    # create table
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {username} (id INTEGER PRIMARY KEY, password TEXT, balance INTEGER)")
    conn.commit()
    cursor.close()
    conn.close()

def signup(username: str, password: int) -> None:
    # check if the pin is 4 digits
    if len(str(password)) != 4:
        raise ValueError("Pin should be 4 digits.")
    else:
        # connect to the database
        conn = sqlite3.connect('db/atm.db')
        create_table(username)
        cursor = conn.cursor()
        # hash the password
        password = hashlib.sha256(str(password).encode()).hexdigest()
        # insert user's data into the table
        cursor.execute(f"INSERT INTO {username} (password) VALUES (?)", (password,))
        cursor.execute(f"INSERT INTO {username} (balance) VALUES (0)")
        conn.commit()
        cursor.close()
        conn.close()

def login(username: str, password: int) -> bool:
    # check if the pin is 4 digits
    if len(str(password)) != 4:
        raise ValueError("Pin should be 4 digits.")
    # connect to the database
    conn = sqlite3.connect('db/atm.db')
    cursor = conn.cursor()
    # hash the password
    password = hashlib.sha256(str(password).encode()).hexdigest()
    # check if user exists in the table
    cursor.execute(f"SELECT password FROM {username} WHERE password = ?", (password,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result is None:
        return False
    return password == result[0]

def user_setup(username: str, password: int) -> None:
    # create user table if it doesn't exist
    create_table(username)
    # signup or login
    if login(username, password):
        print("Successful login.")
    else:
        print("Welcome, new user! Signing up...")
        signup(username, password)
        print("Successful signup.")

# def change_password(username: str, old_password: int, new_password: int) -> bool:
#     # check if the pin is 4 digits
#     if len(str(old_password)) != 4 or len(str(new_password)) != 4:
#         raise ValueError("Pin should be 4 digits.")
#     # connect to the database
#     conn = sqlite3.connect('db/atm.db')
#     cursor = conn.cursor()
#     # hash the old password for comparison
#     old_password = hashlib.sha256(str(old_password).encode()).hexdigest()
#     # check if user exists in the table
#     cursor.execute(f"SELECT password FROM {username} WHERE password = ?", (old_password,))
#     result = cursor.fetchone()
#     if result is None:
