# Challenge
# • The letter a becomes 4
# • The letter b becomes 8
# • The letter e becomes 3
# • The letter l becomes 1
# • The letter o becomes 0
# • The letter s becomes 5
# • The letter t becomes 7

name = input("Enter some text: ")
haxor = name.replace("a", "4").replace("b", "8").replace("e", "3").replace(
    "l", "1").replace("o", "0").replace("s", "5").replace("t", "7")

print(f"Result: {haxor}")
