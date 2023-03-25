# 1. Create a float object named weight with the value 0.2, and create
# a string object named animal with the value "newt". Then use these
# objects to print the following string using only string concatena-
# tion:
# 0.2 kg is the weight of the newt.
# 2. Display the same string by using the .format() method and empty
# {} place-holders.
# 3. Display the same string using an f-string

weight = 0.2
animal = "newt"

print(str(weight) + " is the weight of the " + animal)
print("{} is the weight of the {}".format(weight, animal))
print(f"{weight} is the weight of the {animal}")
