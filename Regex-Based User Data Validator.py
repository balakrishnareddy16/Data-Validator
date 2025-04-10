import re

# Dictionary for month names
months = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

# Name
while True:
    pattern = re.compile(r'^[A-Za-z ]+$')
    text = input("Enter Your Name: ")
    res = pattern.fullmatch(text)
    if res is not None:
        name = res.group()
        break
    else:
        print("Enter Name in Correct Format !")

# Date of Birth
while True:
    pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
    text = input("Enter Date of Birth (DD-MM-YYYY): ")
    res = pattern.fullmatch(text)
    if res is not None:
        dob = res.group()
        break
    else:
        print("Enter DOB in Correct Format !")

# Email id
while True:
    pattern = re.compile(r'[a-z0-9]+@gmail.com\Z')
    text = input("Enter Email id: ")
    res = pattern.fullmatch(text)
    if res is not None:
        mailid = res.group()
        break
    else:
        print("Enter Mail id in correct format !")

# Mobile Number
while True:
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    text = input("Enter Mobile Number (XXX-XXX-XXXX): ")
    res = pattern.fullmatch(text)
    if res is not None:
        mobile = res.group()
        break
    else:
        print("Enter Mobile Number in correct Format !")

# Extract DOB components
day, month, year = dob.split('-')
month_name = months.get(month, "Invalid")

# Output
print(f"\nName : {name}")
print(f"Birth day is {day}")
print(f"Birth month is {month_name}")
print(f"Birth year is {year}")
print(f"Mail id: {mailid}")
print(f"Mobile : {mobile.replace('-', '')}")
