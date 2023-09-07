import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |

=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# Step 1

word_list = ["aardvark", "baboon", "camel", "apple", "flower", "queen", "mashroom", "neighbord"]
chosen_word = random.choice(word_list)
print(chosen_word)
# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

lives = 6
the_end = False

list_word = []
for _ in range(0, len(chosen_word)):
    list_word += "_"
    # if len(list_word)==len(chosen_word):
    #   print(list_word)

# TODO-2: - Loop through each position in the chosen_word;

while not the_end:
    guess = input("Guess the letter,please: ").lower()

    if guess in list_word:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

        if letter == guess:
            list_word[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.", stages[lives])

        lives -= 1
        if lives == 0:
            the_end = True
            print("You lose.")

    print(f"{' '.join(list_word)}")

    if "_" not in list_word:
        the_end = True
        print("You are winner.")

