import random
import tkinter as tk
from tkinter import messagebox

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentplayer = "X"
Winner = None
gamerunning = True
player_score = 0
computer_score = 0
dark_mode = False

# GUI functions
def update_buttons():
    for i, button in enumerate(buttons):
        if dark_mode:
            if board[i] == "X":
                button.config(text="🌞", bg=button_bg, fg=button_fg)
            elif board[i] == "O":
                button.config(text="🌜", bg=button_bg, fg=button_fg)
            else:
                button.config(text=board[i], bg=button_bg, fg=button_fg)
        else:
            button.config(text=board[i], bg=button_bg, fg=button_fg)

def animate_button(button):
    original_color = button.cget("bg")
    for _ in range(3):
        button.config(bg="yellow")
        root.update()
        root.after(100)
        button.config(bg=original_color)
        root.update()
        root.after(100)

def on_button_click(i):
    global currentplayer, gamerunning
    if board[i] == "-" and gamerunning:
        board[i] = currentplayer
        animate_button(buttons[i])
        update_buttons()
        if not checkwin():
            if not checktie():
                switchplayer()
                if currentplayer == "O":
                    computer_move()
                    update_buttons()
                    if not checkwin():
                        checktie()
                        switchplayer()

def printBoard(board):
    for i in range(0, len(board), 3):
        print(board[i] + " | " + board[i + 1] + " | " + board[i + 2])

def checkhorizontle(board):
    global Winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        Winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        Winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        Winner = board[6]
        return True
    return False

def checkrow(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        Winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        Winner = board[2]
        return True
    return False

def checkdiag(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        Winner = board[2]
        return True
    return False

def checktie():
    global gamerunning
    if "-" not in board and gamerunning:
        gamerunning = False
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        restart_game()
        return True
    return False

def checkwin():
    global player_score, computer_score, gamerunning
    if checkdiag(board) or checkhorizontle(board) or checkrow(board):
        gamerunning = False
        messagebox.showinfo("Tic Tac Toe", f"The winner is {Winner}")
        if Winner == "X":
            player_score += 1
        else:
            computer_score += 1
        update_scoreboard()
        restart_game()
        return True
    return False

def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

def minimax(board, depth, is_maximizing):
    if checkdiag(board) or checkhorizontle(board) or checkrow(board):
        return -1 if Winner == "X" else 1 if Winner == "O" else 0
    elif "-" not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = "-"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = "-"
                best_score = min(score, best_score)
        return best_score

def computer_move():
    best_score = -float('inf')
    best_move = 0
    for i in range(9):
        if board[i] == "-":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = "-"
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

def update_scoreboard():
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}", bg=bg_color, fg=fg_color)

def restart_game():
    global board, currentplayer, Winner, gamerunning
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    currentplayer = "X"
    Winner = None
    gamerunning = True
    update_buttons()

def toggle_dark_mode():
    global dark_mode, bg_color, fg_color, button_bg, button_fg
    dark_mode = not dark_mode
    if dark_mode:
        bg_color = "#2E2E2E"
        fg_color = "#FFFFFF"
        button_bg = "#4E4E4E"
        button_fg = "#FFFFFF"
    else:
        bg_color = "#FFFFFF"
        fg_color = "#000000"
        button_bg = "#F0F0F0"
        button_fg = "#000000"
    
    root.config(bg=bg_color)
    for button in buttons:
        button.config(bg=button_bg, fg=button_fg)
    score_label.config(bg=bg_color, fg=fg_color)
    dark_mode_button.config(bg=button_bg, fg=button_fg)
    update_buttons()

# Initial colors
bg_color = "#FFFFFF"
fg_color = "#000000"
button_bg = "#F0F0F0"
button_fg = "#000000"

# GUI setup
root = tk.Tk()
root.title("Tic Tac Toe")
root.config(bg=bg_color)

header_frame = tk.Frame(root, bg=bg_color)
header_frame.grid(row=0, column=0, columnspan=3, pady=10)

dark_mode_button = tk.Button(header_frame, text="🌞/🌜", font=('normal', 20), bg=button_bg, fg=button_fg, command=toggle_dark_mode)
dark_mode_button.pack(side="right")

score_label = tk.Label(header_frame, text=f"Player: {player_score}  Computer: {computer_score}", font=('normal', 20), bg=bg_color, fg=fg_color)
score_label.pack(side="left")

game_frame = tk.Frame(root, bg=bg_color)
game_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

buttons = []
for i in range(9):
    button = tk.Button(game_frame, text=board[i], font=('normal', 40), width=5, height=2, bg=button_bg, fg=button_fg, command=lambda i=i: on_button_click(i))
    button.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(button)

root.mainloop()
