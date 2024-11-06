def personalized_greeting():
    # Ask for user's name
    name = input("What is your name? ")
    
    # Ask for user's favorite color
    color = input("What is your favorite color? ")
    
    # Print personalized greeting
    print(f"Hello, {name}! Your favorite color, {color}, is awesome!")

# Run the personalized greeting function
personalized_greeting()