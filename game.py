import tkinter as tk
from tkinter import messagebox
from joblib import load
import numpy as np 


class TicTacToeGUI:
    def __init__(self, root, model):
        self.root = root
        self.model_path = model
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_ui()

    def create_ui(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_click(self, row, col):
        if self.board[row][col] == '-':
            if self.current_player == 'X':
                self.board[row][col] = 'X'
                self.buttons[row][col].config(text='X', state=tk.DISABLED)
                if self.check_winner('X'):
                    messagebox.showinfo("Game Over", "Player X wins!")
                    self.reset_game()
                    return
                elif self.is_draw():
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.reset_game()
                    return
                self.current_player = 'O'
                self.ai_turn()

    def ai_turn(self):
        flat_board = [1 if cell == 'X' else -1 if cell == 'O' else 0 for row in self.board for cell in row]
        ai_input = np.array([flat_board], dtype=np.float64)
        regressor = load(self.model_path)
        ai_output = regressor.predict(ai_input)[0]

        best_move = int(np.argmax(ai_output))
        row, col = divmod(best_move, 3)

        self.board[row][col] = 'O'
        self.buttons[row][col].config(text='O', state=tk.DISABLED)

        if self.check_winner('O'):
            messagebox.showinfo("Game Over", "Player O wins!")
            self.reset_game()
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
        else:
            self.current_player = 'X'

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != '-' for row in self.board for cell in row)

    def reset_game(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='', state=tk.NORMAL)

if __name__ == '__main__':
    model_choice = int(input("CHOOSE MODEL:\n1. Multilayer Perceptron\n2. KNN\n3. Linear Regression\n"))
    model_path = 'mlp_reg.joblib' if model_choice == 1 else 'knn_reg.joblib' if model_choice == 2 else 'l_reg.joblib'

    root = tk.Tk()
    root.title("Tic Tac Toe")
    game = TicTacToeGUI(root, model_path)
    root.mainloop()

