import random

words = (
    "apple", "banana", "orange", "pineapple", "cat", "dog", "grape", "watermelon", 
    "strawberry", "blueberry", "cherry", "lemon", "kiwi", "peach", "pear", "plum", 
    "melon", "apricot", "applesauce", "bluebird", "elephant", "giraffe", "lion", 
    "tiger", "bear", "kangaroo", "whale", "dolphin", "zebra", "rabbit", "horse", 
    "panda", "parrot", "penguin", "cow", "sheep", "goat", "frog", "squirrel", 
    "bicycle", "train", "airplane", "ship", "car", "motorcycle", "bus", "rocket", 
    "boat", "submarine", "skyscraper", "building", "house", "tree", "forest", 
    "mountain", "river", "desert", "ocean", "planet", "star", "moon", "sun", 
    "earth", "sky", "cloud", "rain", "snow", "wind", "thunder", "lightning"
)


# dictionary of key:()
hangman_art = {
    0: """
        ------
        |    |
        |
        |
        |
        |
    --------""",
    1: """
        ------
        |    |
        |    o
        |
        |
        |
    --------""",
    2: """
        ------
        |    |
        |    o
        |    |
        |
        |
    --------""",
    3: """
        ------
        |    |
        |    o
        |   /|
        |
        |
    --------""",
    4: """
        ------
        |    |
        |    o
        |   /|\\
        |
        |
    --------""",
    5: """
        ------
        |    |
        |    o
        |   /|\\
        |   /
        |
    --------""",
    6: """
        ------
        |    |
        |    o
        |   /|\\
        |   / \\
        |
    --------"""
}


def display_man(wrong_guesses):
    print(hangman_art[wrong_guesses])


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(f"The correct answer is: {answer}")


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try a different one.")
        elif guess not in answer:
            wrong_guesses += 1
            print(f"Wrong guess! You have {6 - wrong_guesses} attempts left.")
        else:
            print(f"Good guess! '{guess}' is in the word.")

        guessed_letters.add(guess)

        # Update the hint with correct guesses
        for i, letter in enumerate(answer):
            if letter == guess:
                hint[i] = guess

        if "_" not in hint:
            print("Congratulations! You've guessed the word!")
            display_answer(answer)
            is_running = False

        if wrong_guesses >= 6:
            print("You've been hanged! Game over.")
            display_answer(answer)
            is_running = False


if __name__ == "__main__":
    main()
