import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg="#121212")
        self.window.geometry("400x580")
        self.window.resizable(False, False)
        
        self.current_player = "X"
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.game_active = True

        self.create_widgets()
    
    def create_widgets(self):
        # Title Header
        self.header_label = tk.Label(self.window, text="TIC TAC TOE", font=("Arial", 30, "bold"), bg="#121212", fg="#FFD700")
        self.header_label.pack(pady=10)

        # Turn display
        self.turn_label = tk.Label(self.window, text="Player X's Turn", font=("Arial", 16), bg="#141414", fg="#FFFFFF")
        self.turn_label.pack(pady=1)

        # Board frame
        self.board_frame = tk.Frame(self.window, bg="#121212")
        self.board_frame.pack(pady=20)

        # Create buttons
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.board_frame, text="", font=("Arial", 24), height=2, width=5,
                    bg="#000000", fg="#FFFFFF", command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                self.board[row][col] = button

        # Result display
        self.result_label = tk.Label(self.window, text="", font=("Arial", 16), bg="#121212", fg="#FFFFFF", padx=10, pady=5)
        self.result_label.pack(pady=5)

        # Reset button
        self.reset_button = tk.Button(
            self.window, text="Play Again", font=("Arial", 14), bg="#1E1E1E", fg="#FFFFFF", command=self.reset_game
        )
        self.reset_button.pack(pady=5)
    
    def make_move(self, row, col):
        """Handles player moves and game logic."""
        if not self.game_active or self.board[row][col]["text"] != "":
            return
        
        self.board[row][col]["text"] = self.current_player
        
        # Change background color based on player
        if self.current_player == "X":
            self.board[row][col].config(bg="#1e264a")  # Blue
        else:
            self.board[row][col].config(bg="#321e4a")  # Purple

        if self.check_winner(row, col):
            self.result_label.config(text=f"Player {self.current_player} Wins!", 
                                    bg="#1e264a" if self.current_player == "X" else "#321e4a")
            self.game_active = False
        elif self.is_draw():
            self.result_label.config(text="It's a Draw!", bg="#555555")  # Neutral gray for draw
            self.game_active = False
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            self.turn_label.config(text=f"Player {self.current_player}'s Turn")
    
    def check_winner(self, row, col):
        """Checks for a winner."""
        # Check row
        if all(self.board[row][c]["text"] == self.current_player for c in range(3)):
            return True
        # Check column
        if all(self.board[r][col]["text"] == self.current_player for r in range(3)):
            return True
        # Check diagonals
        if row == col and all(self.board[i][i]["text"] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2-i]["text"] == self.current_player for i in range(3)):
            return True
        return False
    
    def is_draw(self):
        """Checks if the game is a draw."""
        return all(self.board[r][c]["text"] != "" for r in range(3) for c in range(3))
    
    def reset_game(self):
        """Resets the game to its initial state."""
        self.current_player = "X"
        self.game_active = True
        self.result_label.config(text="", bg="#121212")  # Reset result background to dark mode
        self.turn_label.config(text="Player X's Turn")
        for row in self.board:
            for button in row:
                button.config(text="", bg="#000000")  # Reset to dark mode
    
    def run(self):
        """Runs the game."""
        self.window.mainloop()

# Run the Tic Tac Toe game
if __name__ == "__main__":
    TicTacToe().run()