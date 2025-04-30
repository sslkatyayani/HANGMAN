import random

words = ["python", "developer", "hangman", "script", "keyboard"]
word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6

print("Welcome to Hangman!")

while attempts > 0 and '_' in guessed:
    print("\nWord:", ' '.join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

if '_' not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("You lost! The word was:", word)