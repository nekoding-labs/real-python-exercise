# Write a script named first_letter.py that first prompts the user for
# input by using the string "Tell me your password:" The script should
# then determine the first letter of the user’s input, convert that letter
# to upper-case, and display it back

answer = input("Tell me your password: ")
print(answer[0].upper())
