print("                                          Welcome to the Quiz Program!                                           ")

start = input("Do you want to start the quiz? (yes/no): ").lower()

if start == "yes":
    print("Great! Let's start the quiz.")

    score = 0

    question1 = input("What is the capital of France? ").lower()
    if question1 == "paris":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The answer is Paris.")

    question2 = input("What planet is known as the jewel of the solar system? ").lower()
    if question2 == "saturn":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The answer is Saturn.")

    question3 = input("What is the largest ocean on Earth? ").lower()
    if question3 == "pacific ocean":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The answer is Pacific Ocean.")

    question4 = input("What is the first civilization in the world? ").lower()
    if question4 == "sumerian":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The answer is Sumerian.")

    question5 = input("What is the largest desert in the world? ").lower()
    if question5 == "sahara":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The answer is Sahara.")

    print("Quiz completed!")

    if score >= 3:
        print("Congratulations! You scored", score, "out of 5. You passed the quiz.")
    else:
        print("You scored", score, "out of 5. You failed the quiz.")

    if score == 5:
        print("Excellent! You got a perfect score!")

else:
    print("Okay, maybe next time!")