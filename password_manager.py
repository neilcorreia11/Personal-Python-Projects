from cryptography.fernet import Fernet


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fern_key = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("Username:", user, "| Password:", fern_key.decrypt(password.encode()).decode())


def add():
    name = input("Name: ")
    passwords = input("Password: ")
    with open("passwords.txt", "r") as f:
        f.write(name + "|" + fern_key.encrypt(passwords.encode()).decode())


while True:
    mode = input("View existing password or create new password?(view, add): ")
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
