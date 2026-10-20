import hashlib
import json

def register():

    # This function is used to register a new user.
    # It takes an email and a password as input, with the password being stored in the database as a hash.
    # The function includes subsystems designed to test code segments for errors and handle them in a controlled manner, preventing the program from terminating.

    print("\n ==-- USER REGISTER --==")
    email = input("Insert email ").strip()
    password = input("Insert password ").strip()

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    try:
        with open("database.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    for user in data:
        if user["email"] == email:
            print("Error, User already registered")
            return

    new_user = {
        "email": email,
        "password": password_hash
    }
    data.append(new_user)

    with open("database.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    print("User registered successfully")

def login():

    # This function handles the user login process by verifying the existence of the email address and, if found, validating the hashed password.

    print("\n ==-- LOGIN --==")
    email = input("Insert email ").strip()

    try:
        with open("database.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("Error, no user registered")
        return

    for user in data:
        if user["email"] == email:

            password = input("Insert password ").strip()
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            if user["password"] == password_hash:
                print("Login successful")
                return
            else:
                print("Password incorrect")

    print("Email not found")

def menu():

    # This function constitutes the body of the menu.
    # It essentially uses a loop, where each selection calls its corresponding function.

    while True:
        print("\n ===- MENU -===")
        print("1. Register User")
        print("2. Login")
        print("3. Exit")

        option = input("Select an option: ").strip()

        if option == "1":
            register()
        elif option == "2":
            login()
        elif option == "3":
            break
        else:
            print("Invalid option")

menu()