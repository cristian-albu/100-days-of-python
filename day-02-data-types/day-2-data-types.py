# age = int(input("What is your current age?"))

# yearsLeft = 90 - age
# months_left = (90 - age) * 12
# days_left = (90 - age) * 365

# print(f"You have {yearsLeft} years, {months_left} months, {days_left} days left")


total = float(input("Welcome the the tip calculator\nWhat was the total bill? "))
tip_percent = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

print(f"Each person should pay ${round((total * tip_percent / 100 + total) / people, 2)}")