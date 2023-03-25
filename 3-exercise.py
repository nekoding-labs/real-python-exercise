# 1. Write a script that takes input from the user and displays that in-
# put back.
# 2. Write a script that takes input from the user and displays the input
# in lowercase.
# 3. Write a script that takes input from the user and displays the num-
# ber of characters inputted

stdin = input("Whats your name? ")
print("your respond:", stdin.strip())

print("lower case version: ", stdin.lower())

print("answer length:", len(stdin))
