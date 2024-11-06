def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
            "answer": "c"
        },
        {
            "question": "Which language is known as the language of the web?",
            "choices": ["a) Python", "b) JavaScript", "c) Java", "d) C++"],
            "answer": "b"
        },
        {
            "question": "What color is the sky?",
            "choices": ["a) Blue", "b) Red", "c) Yellow", "d) Green"],
            "answer": "a"
        }
    ]

    def play_quiz():
        score = 0
        for q in questions:
            print(q["question"])
            for choice in q["choices"]:
                print(choice)
            answer = input("Your answer: ").lower()
            if answer == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer']}.\n")

        print(f"Your final score is {score} out of {len(questions)}.")

    while True:
        play_quiz()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Run the quiz game function
quiz_game()
