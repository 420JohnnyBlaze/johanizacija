import random
import string
import sqlite3

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def store_password(service, username, password):
    with sqlite3.connect('passwords.db') as conn:

        conn.execute('INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)', 
                       (service, username, password))

def retrieve_passwords():
    with sqlite3.connect('passwords.db') as conn:
        return conn.execute('SELECT service, username, password FROM passwords').fetchall()

if __name__ == "__main__":
    action = input("Do you want to store a new password or retrieve existing ones? (store/retrieve): ").strip().lower()
    if action == "store":
        service = input("Enter the service name: ")
        username = input("Enter the username: ")
        length = int(input("Enter the length of the password: "))
        password = generate_password(length)
        store_password(service, username, password)
        print(f"Stored Password: {password}")
    elif action == "retrieve":
        passwords = retrieve_passwords()
        for service, username, password in passwords:
            print(f"Service: {service}, Username: {username}, Password: {password}")
    else:
        print("Invalid action. Please choose 'store' or 'retrieve'.")
