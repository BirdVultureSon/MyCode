import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Крестики-нолики")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []
        
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=3, command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)
        
    def on_click(self, i, j):
        index = i * 3 + j
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.show_winner()
            elif " " not in self.board:
                self.show_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                                [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                                [0, 4, 8], [2, 4, 6]]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False
    
    def show_winner(self):
        winner = self.current_player
        tk.messagebox.showinfo("Победитель", f"Игрок {winner} победил!")
        self.reset_game()
    
    def show_draw(self):
        tk.messagebox.showinfo("Ничья", "Ничья! Начните новую игру.")
        self.reset_game()
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text="")
        
    def run(self):
        se