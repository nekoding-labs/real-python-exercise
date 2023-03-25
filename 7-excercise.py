# 1. Write a script that asks the user to input a number and then dis-
# plays that number rounded to two decimal places. When run, your
# program should look like this:
# Enter a number: 5.432
# 5.432 rounded to 2 decimal places is 5.43

# 2. Write a script that asks the user to input a number and then dis-
# plays the absolute value of that number. When run, your program
# should look like this:
# Enter a number: -10
# The absolute value of - 10 is 10.0

# 3. Write a script that asks the user to input two numbers by using the
# input() function twice, then display whether or not the difference
# between those two number is an integer. When run, your program

num = input("Enter a number: ")
print(f"{num} rounded to 2 decimal places is {round(float(num), 2)}")


absolute = input("Enter a number: ")
print(f"The absolute value of {absolute} is {abs(int(absolute))}")

a = input("Enter a number: ")
b = input("Enter another number: ")

c = round(float(a), 2)
d = round(float(b), 2)

result = c - d
print(
    "The difference between {a} and {b} is an integer? {result}".format(a=c, b=d, result=result.is_integer()))
