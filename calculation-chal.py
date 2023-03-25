# Write a script called exponent.py that receives two numbers from the
# user and displays the first number raised to the power of the second
# number.

a = input("Enter a base: ")
b = input("Enter an exponent: ")

calc = float(a) ** float(b)
result = "{a} to the power of {b} = {result}".format(a=a, b=b, result=calc)
print(result)
