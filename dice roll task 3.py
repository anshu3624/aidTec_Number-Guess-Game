import tkinter as tk
import random

class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")
        
        self.label = tk.Label(root, text="Number of Dice:")
        self.label.pack()

        self.dice_count_entry = tk.Entry(root)
        self.dice_count_entry.pack()

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def roll_dice(self):
        try:
            num_dice = int(self.dice_count_entry.get())
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.")
            return

        if num_dice <= 0:
            self.result_label.config(text="Please enter a positive number of dice.")
            return

        results = [random.randint(1, 6) for _ in range(num_dice)]
        result_text = f"Results: {', '.join(map(str, results))}"
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()
