# 1. In one line of code, display the result of trying to .find() the sub-
# string "a" in the string "AAA". The result should be -1.
# 2. Replace every occurrence of the character "s" with "x" in the string
# "Somebody said something to Samantha.".
# 3. Write and test a script that accepts user input using the input()
# function and displays the result of trying to .find() a particular
# letter in that input.

test = "AAA"
print(test.find("a"))

test = "Somebody said something to Samantha."
print(test.replace("s", "x"))

inp = input("tipe hewan peliharaan? ")
print("Kucing?", inp.find("kucing"))
