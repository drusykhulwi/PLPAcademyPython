person = {}
# Ask the user for input and store the information in the dictionary
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
person['favorite_color'] = input("Enter your favorite color: ")
# Print the dictionary to the console
print("Person Information:")
for key, value in person.items():
   print(f"{key}: {value}")


