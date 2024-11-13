# Store a list of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Use list comprehension to create a new list with words having an odd number of characters
odd_words = [word for word in words if len(word) % 2 != 0]

# Print the new list
print(f"Words with an odd number of characters: {odd_words}")


