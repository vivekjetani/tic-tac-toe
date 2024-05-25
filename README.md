
# Tic Tac Toe Game with Tkinter

This is a Tic Tac Toe game implemented using Python's Tkinter library. The game can be played between a human player and the computer.

## Features

- Player vs. Computer gameplay
- Score tracking for both player and computer
- Dark mode toggle
- Animated button clicks
- Minimax algorithm for computer moves

## Game Rules

1. The game is played on a 3x3 grid.
2. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
3. The player starts first as 'X', and the computer plays as 'O'.

## How to Run

1. Ensure you have Python installed on your machine.
2. Install Tkinter if it is not already installed. You can install it using the following command:
    ```
    pip install tk
    ```
3. Save the provided code to a file, e.g., `tic_tac_toe.py`.
4. Run the script using the command:
    ```
    python tic_tac_toe.py
    ```

## Dark Mode

You can toggle between light and dark mode using the button labeled with sun and moon icons (🌞/🌜).

## Implementation Details

- The game board is represented by a list of 9 elements.
- The Minimax algorithm is used for the computer's moves to ensure optimal play.
- The GUI is built using Tkinter and updates dynamically based on game state.

## Functions

- `update_buttons()`: Updates the text and color of the buttons based on the current board state and mode.
- `animate_button(button)`: Animates the button when clicked.
- `on_button_click(i)`: Handles the button click events, updates the board, and checks for game status.
- `printBoard(board)`: Prints the current state of the board to the console.
- `checkhorizontle(board)`, `checkrow(board)`, `checkdiag(board)`: Check for win conditions.
- `checktie()`: Checks if the game is a tie.
- `checkwin()`: Checks if there is a winner.
- `switchplayer()`: Switches the current player.
- `minimax(board, depth, is_maximizing)`: Minimax algorithm for determining the best move for the computer.
- `computer_move()`: Determines and makes the best move for the computer.
- `update_scoreboard()`: Updates the score display.
- `restart_game()`: Resets the game state for a new game.
- `toggle_dark_mode()`: Toggles between light and dark mode.



## License

This project is licensed under the MIT License.
