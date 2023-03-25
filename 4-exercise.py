# 1. Create a string containing an integer, then convert that string into
# an actual integer object using int(). Test that your new object is
# a number by multiplying it by another number and displaying the
# result.
# 2. Repeat the previous exercise, but use a floating-point number and
# float().
# 3. Create a string object and an integer object, then display them side-
# by-side with a single print statement by using the str() function.
# 4. Write a script that gets two numbers from the user using the
# input() function twice, multiplies the numbers together, and
# displays the result. If the user enters 2 and 4, your program should
# print the following text:
# The product of 2 and 4 is 8.0.

strint = "20"
print(int(strint))

strfloat = "20.0"
print(float(strfloat))

print(str(int), str(float))

a = input("input a: ")
b = input("input b: ")

template = "The product of {} and {} is {result:.2f}"
print(template.format(a, b, result=float(a) * float(b)))
