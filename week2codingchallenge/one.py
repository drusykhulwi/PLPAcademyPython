# Accept user input to create a list of integers
numbers = input("Enter a list of integers separated by spaces: ")
integer_list = [int(num) for num in numbers.split()]
# Compute the sum of all the integers in the list
total_sum = sum(integer_list)
# Print the sum
print(f"The sum of the integers is: {total_sum}")

