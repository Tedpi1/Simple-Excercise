
import datetime

def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

birthdate = datetime.date(input('enter date of Birth'))
age = calculate_age(birthdate)
print("The age is:", age)