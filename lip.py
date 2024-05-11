
import datetime

def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

birthdate = datetime.date(1990, 5, 15)
age = calculate_age(birthdate)
print("The age is:", age)