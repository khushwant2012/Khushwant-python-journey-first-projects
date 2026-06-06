import random

print("\n🎮 Welcome to Hangman!\n")

wordlist = ['aardvark', 'baboon', 'camel']
chosen_word = random.choice(wordlist)

display = ['_' for _ in chosen_word]

lives = 6

stages = [
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
      |
      |
      |
      |
=========
"""
]

guessed_letters = []

game_over = False

while not game_over:

    print("\n" + stages[lives])
    print("Word: ", " ".join(display))
    print("Lives:", lives)
    print("Guessed letters:", guessed_letters)

    guess = input("\n👉 Guess a letter: ").lower()

    # handle repeated guess
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # check guess
    if guess not in chosen_word:
        lives -= 1
        print("❌ Wrong guess!")

        if lives == 0:
            print(stages[lives])
            print("\n💀 You lost! The word was:", chosen_word)
            game_over = True

    # update display
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    # win check
    if "_" not in display:
        print("\n🎉 You win! The word was:", chosen_word)
        game_over = True