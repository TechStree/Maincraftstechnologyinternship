# Take input from the user
num = int(input("Enter a number: "))

# Store the original number for comparison later
original_num = num

# Find the number of digits in the number
num_digits = len(str(num))

# Initialize a variable to store the sum of powers of digits
sum_of_powers = 0

# Process each digit one by one
while num > 0:
    digit = num % 10           # Get the last digit
    sum_of_powers += digit ** num_digits  # Raise digit to power of num_digits and add to sum
    num = num // 10            # Remove the last digit

# Compare the sum with the original number
if sum_of_powers == original_num:
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is not an Armstrong number")
