# num1 = 20
# num2 = 30
# num3 = 40
#
# max = num1 if num1>num2 else num2
#
# print(max)

# Input three numbers
num1 = 250
num2 = 10
num3 = 20
num4 = 880
num5 = 220

# Find the largest number using conditional statements
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
elif (num3 >= num2) and (num3 >= num4):
    largest = num3
elif (num4 >= num3) and (num4 >= num5):
    largest = num4
else:
    largest = num5

print(f"The largest number is {largest}")
