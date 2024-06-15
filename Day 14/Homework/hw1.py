# Homework: Make 5 examples of While Loop

# 1) This loop starts at 2 and adds 2 each time until it reaches 10.
ffff = 2
while ffff <= 10:
    print(ffff)
    ffff = ffff + 2

# 2) This loop starts at 1 and adds 2 each time until it reaches 100.
ო = 1
while ო <= 100:
    print(ო)
    ო = ო + 2

# 3) This loop counts down from 10 to 1.
countdown = 10
while countdown > 0:
    print(countdown)
    countdown = countdown - 1
print("Done!")

# 4) This loop starts at 1 and prints numbers until it reaches 5.
num = 1
while num <= 5:
    print(num)
    num = num + 1

# 5) This loop asks for input until the user types 'exit'.
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Type 'exit' to stop the loop: ")
    print("You typed:", user_input)
