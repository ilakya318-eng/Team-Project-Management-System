# User Authentication Module

def authenticate_user(username, password):

    if username == "admin" and password == "admin123":
        print("Login Successful")
        return True

    else:
        print("Invalid Username or Password")
        return False


print("===== USER LOGIN =====")

username = input("Enter Username: ")
password = input("Enter Password: ")

authenticate_user(username, password)
