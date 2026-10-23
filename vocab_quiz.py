import random

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
    words = list(VOCAB.items())
    random.shuffle(words)
    score = 0

    for word, meaning in words:
        answer = input(f"What is '{word}' in English? ")
        if check_answer(answer, meaning):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The answer is: {meaning}")

    print(f"\nFinal score: {score}/{len(words)}")


if __name__ == "__main__":
    main()
