# 1. Write a script that converts the following strings to lowercase: "Animals", "Badger", "Honey Bee", "Honeybadger". Print each lowercase
# string on a separate line.
# 2. Repeat Exercise 1, but convert each string to uppercase instead of
# lowercase.
# 3. Write a script that removes whitespace from the following strings:
# string1 = " Filet Mignon"
# string2 = "Brisket "
# string3 = " Cheeseburger "
# Print out the strings with the whitespace removed.
# 4. Write a script that prints out the result of .startswith("be") on each
# of the following strings:
# string1 = "Becomes"
# string2 = "becomes"
# string3 = "BEAR"
# string4 = " bEautiful"
# 5. Using the same four strings from Exercise 4, write a script that
# uses string methods to alter each string so that .startswith("be")
# returns True for all of them.

s1, s2, s3, s4 = "Animals", "Badger", "Honey Bee", "Honeybadger"
print(s1.lower(), s2.lower(), s3.lower(), s4.lower())

print(s1.upper(), s2.upper(), s3.upper(), s4.upper())

string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "

print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

print(
    string1.startswith("be"),
    string2.startswith("be"),
    string3.startswith("be"),
    string4.startswith("be")
)

print(
    string1.lower().strip().startswith("be"),
    string2.lower().strip().startswith("be"),
    string3.lower().strip().startswith("be"),
    string4.lower().strip().startswith("be")
)
