from datetime import datetime


class Birthday:
    def __init__(self, birthdate):
        self.birthdate = birthdate

    def today_date(self):
        today = datetime.today()
        format_birthdate = list(map(int, self.birthdate.split('/')))  # create a list and split date input with '/'
        if format_birthdate[1] > 12 or format_birthdate[2] > 31:  # check month and day that user input
            return "WRONG"
        else:
            birth_date = datetime.strptime(self.birthdate, "%Y/%m/%d")
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age


user_birth_date = input()  # get date from user
user_age = Birthday(user_birth_date)  # create a object
print(user_age.today_date())
