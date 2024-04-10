import re
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="username_and_password"
)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def check(email):  # Checks the email the user enters, returns True if the format is correct, otherwise returns False.
    if re.fullmatch(regex, email):
        return True

    else:
        return False


def get_password():  # Check the input password, this password must contain both letters and numbers, if this condition
    # is correct, return the password, otherwise the user must re-enter the password.
    while True:
        user_password = input("Enter a password (must contain both letters and numbers): ")
        if re.search(r'\d', user_password) and re.search(r'[a-zA-Z]', user_password):
            return user_password

        else:
            print("Password must contain both letters and numbers. Try again.")
            continue


if __name__ == '__main__':
    while True:
        # Enter the email
        user_name = input('enter your email:')
        # check username
        if check(user_name):
            password = get_password()
            print(f'your email is {user_name} and password is {password}')
            # if username and password is correct, we save these informations into the database
            cursor = mydb.cursor()
            sql = "INSERT INTO user_information (username, password) VALUES (%s, %s)"
            val = (user_name, password)
            cursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            break
        else:
            print("Invalid Email, Please enter correct email(expression@string.string)")
            continue




