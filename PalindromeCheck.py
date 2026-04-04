# Take user input
user_input = input("Enter a string: ")

# Check if the string is a palindrome
if user_input == user_input[::-1]:
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")
