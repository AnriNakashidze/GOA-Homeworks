# Homework: Create 5 examples of If and Else statements

# 1) Check if a number is less than 10.
num = 7
if num < 10:
    print("The number is less than 10.")
else:
    print("The number is 10 or greater.")

# 2) Determine if a number is odd or even.
num = 3
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 3) Check if it's currently raining.
is_raining = True
if is_raining:
    print("It's raining outside. Take an umbrella.")
else:
    print("No rain at the moment. Enjoy the weather!")

# 4) Verify if a person meets the driving age requirement.
age = 16
driving_age = 18
if age >= driving_age:
    print("You are old enough to drive.")
else:
    print("You are not yet old enough to drive.")

# 5) Check if a password matches the expected input.
password = "secret"
input_password = "password123"
if input_password == password:
    print("Access granted.")
else:
    print("Access denied.")
