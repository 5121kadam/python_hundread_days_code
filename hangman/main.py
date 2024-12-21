import random
from hangman_word import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
lives = 6
print(logo)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter ").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}.")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        print(f"********** {lives}/6 lives left **********")
        if lives == 0:
            game_over = True
            print(f"********** It was {chosen_word}. You Lose! **********")
    print(stages[lives])
    print(display)
    if "_" not in display:
        print("You Win!")
        game_over = True