VOCAB = {
    "aso": "dog",
    "pusa": "cat",
    "bahay": "house",
    "tubig": "water",
    "kaibigan": "friend",
}


def check_answer(user_answer, correct):
    return user_answer.strip().lower() == correct.lower()


def main():
    for word, meaning in VOCAB.items():
        answer = input(f"What is '{word}' in English? ")
        if check_answer(answer, meaning):
            print("Correct!")
        else:
            print(f"Wrong. The answer is: {meaning}")


if __name__ == "__main__":
    main()
