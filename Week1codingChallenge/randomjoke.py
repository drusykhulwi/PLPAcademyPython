import random

def random_joke_generator():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why do developers wear glasses? Because they don't see sharp.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "What is a programmer's favorite hangout place? Foo Bar."
    ]

    # Select a random joke
    joke = random.choice(jokes)
    
    # Print the selected joke
    print(joke)

# Run the random joke generator function
random_joke_generator()
