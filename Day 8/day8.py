false_1 = 5 < 2
false_2 = 10 == 3
false_3 = 15 > 20
false_4 = 7 <= 4
false_5 = 9 >= 12
print(false_1)
print(false_2)
print(false_3)
print(false_4)
print(false_5)

true_1 = 3 < 5
true_2 = 10 == 10
true_3 = 15 > 10
true_4 = 7 <= 7
true_5 = 9 >= 5
print(true_1)
print(true_2)
print(true_3)
print(true_4)
print(true_5)


# Examples of 'and' operator
print(True and True)        # True
print(True and False)       # False
print(False and True)       # False
print(False and False)      # False
print(5 > 3 and 3 < 5)      # True
print(5 > 3 and 3 > 5)      # False
print(3 == 3 and 4 == 4)    # True
print(3 == 3 and 4 == 5)    # False
print(10 > 2 and 2 > 1)     # True
print(8 > 5 and 7 < 10)     # True

# Examples of 'or' operator
print(True or True)         # True
print(True or False)        # True
print(False or True)        # True
print(False or False)       # False
print(5 > 3 or 3 < 5)       # True
print(5 > 3 or 3 > 5)       # True
print(3 == 3 or 4 == 4)     # True
print(3 == 3 or 4 == 5)     # True
print(10 < 2 or 2 > 1)      # True
print(8 < 5 or 7 < 10)      # True
