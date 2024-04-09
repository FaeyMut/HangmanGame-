Python hangman game with GUI
Game logic:
 core logic for processing guesses, 
 managing game states,
 determining win or loss conditions

 Dynamic UI Updates: 
  Tkinter to update game interface

Event handling: event listeners to capture user input

HANGMAN GAME MECHANICS:
involves guessing a word by identifying individual letters
Asecret word is chosen which the player attempts to guesses
the player has limited number of incorrect guesses before game is lost
each corect guess reveals the position of the letter in the word
incorrect guesses bring the player one step closer to losing
 as parts of the hangman are drawn

Implementing game logic:
managing secret word, trqcking player guesses determine the game
outcome using python

Tkinter is ued to set p the GUI for the hangman game
oop approach to enhance structure and maintainability of code

python -m tkinter

hangman_game.py contains GUI components and game logic
hangmanGame class encaspulates both game logic and GUI components

main aplication window master

Designing layout:
  top section for hangman drawing
  middle section to reveal the words being guessed and blanks for words yet to be guessed
  bottom section with buttons for player input

  tkinter canvas widget for hangman drawing

  incorrect_guesses_count = len(self.incorrect_guesses)
        if incorrect_guesses_count >= 1:
            self.hangman_canvasangman_canvas.create_line(50, 180, 150, 180) #Base
        #additional drawing logic here for each part of the hangman



Importing Libraries: The code imports the Tkinter library (tk) for creating the GUI and the random module for 
selecting a random word from a list.

HangmanGame Class: This class encapsulates the Hangman game logic and GUI setup.

Initialization: The __init__ method sets up the game window, initializes game parameters such as the list of words, the chosen secret word, 
sets of correct and incorrect guesses, and the number of attempts left. It then calls the initialize_gui() method to set up the GUI elements.

Initialize GUI: The initialize_gui() method sets up various GUI elements such as the canvas for displaying the Hangman figure, 
labels for displaying the word with underscores representing unknown letters, buttons for guessing letters, and a reset button.

Setup Alphabet Buttons: The setup_alphabet_buttons() method creates buttons for each letter of the alphabet. 
These buttons allow the player to guess letters by clicking on them.

Choosing Secret Word: The choose_secret_word() method selects a random word from the predefined list of words.

Updating Hangman Canvas: The update_hangman_canvas() method updates the Hangman figure on the canvas based on the number of incorrect guesses.

Drawing Hangman Parts: There are separate methods for drawing each part of the Hangman figure on the canvas (draw_head(), draw_body(), etc.).

Guessing a Letter: The guess_letter() method is called when a player guesses a letter. 
It checks if the letter is in the secret word, updates the game state accordingly, and checks if the game is over.

Updating Word Display: The update_word_display() method updates the displayed word with guessed letters revealed.

Checking Game Over: The check_game_over() method checks if the game is over by either winning or losing conditions.

Displaying Game Over Message: The display_game_over_message() method displays a message indicating whether the player won or lost the game.

Resetting the Game: The reset_game() method resets the game parameters and GUI elements for a new game.

Main Function: The main() function creates an instance of the tk.Tk() class (representing the main window), 
instantiates the HangmanGame class, and starts the Tkinter event loop.

Conditional Execution: The if __name__ == "__main__": block ensures that the main() function is executed only when the script is run directly.

In summary, this code creates a Hangman game with a graphical user interface using Tkinter, 
allowing players to guess letters to uncover a hidden word while providing visual feedback on the progress of the game.






