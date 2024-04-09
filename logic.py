import random

#potential secret words
word_list = ["python", "hangman", "programming", "coding"]

#randomly select a secret word from the list
secret_word = random.choice(word_list)

#initialize variables to track guesses and attempts
correct_guesses = set()
incorrect_guesses = set()
attempts_left = 6

#function to display current game state
def display_game_state():
    #display secret word with guessed letters revealed
    displayed_word = "".join([letter if letter in correct_guesses else "_" for letter in secret_word])
    print(f"Word: {displayed_word}")
    print(f"Incorrect Guesses: {' '.join(incorrect_guesses)}")
    print(f"Attempts Left: {attempts_left}")

#main game loop
while True:
    display_game_state()
    guess = input("Enter your guess: ").lower()

    #check if the guess is in the secret word
    if guess in secret_word:
        correct_guesses.add(guess)
        #check for win condition
        if set(secret_word).issubset(correct_guesses):
            print("Congratulations! You've guessed the word.")
            break
        else:
            incorrect_guesses.add(guess)
            attempts_left -= 1
            #check for lose condition
            if attempts_left == 0:
                print("Game Over! You've run out of attempts.")
                print(f"The secret word was: {secret_word}")
                break
            