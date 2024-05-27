# String, Float -->> Integer
int1 = int("23535")
int2 = int(5252.3)
int3 = int("2525")
int4 = int(22221.412)
int5 = int("523")

# Integer, Float -->> String
str1 = str(99011334)
str2 = str(5252.3)
str3 = str(234234122)
str4 = str(22221.412)
str5 = str(13951823958)

# Integer, String -->> Float
float1 = float(523)
float2 = float("12345.67")
float3 = float("45678.32")
float4 = float("9876.54")
float5 = float("876.54321")

# Float, String -->> Integer
int6 = int(9876.54)
int7 = int("34567")
int8 = int(6543.21)
int9 = int("89012")
int10 = int(12345.67)

# String, Integer -->> Float
float6 = float("6789.01")
float7 = float(54321)
float8 = float("9876.54")
float9 = float(4321)
float10 = float("12345.67")

# Integer, Float -->> String
str6 = str(54321)
str7 = str(1234.56)
str8 = str(98765432)
str9 = str(3210.87)
str10 = str(87654321)

# Float, Integer -->> String
str11 = str(210.45)
str12 = str(34567)
str13 = str(4321.23)
str14 = str(67890)
str15 = str(54321.89)

# Float, String -->> Integer
int11 = int(6789.01)
int12 = int("4321")
int13 = int(9876.54)
int14 = int("12345")
int15 = int(1234.56)


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))
num4 = int(input("Enter a fourth number: "))
num5 = int(input("Enter a final number: "))

print("Sum:", num1 + num2 + num3 + num4 + num5)
print("Subtraction:", num1 - num2 - num3 - num4 - num5)
print("Multiplication:", num1 * num2 * num3 * num4 * num5)
print("Integer Division:", num1 // num2 // num3 // num4 // num5)
print("Float Division:", num1 / num2 / num3 / num4 / num5)
print("Modulo:", num1 % num2 % num3 % num4 % num5)