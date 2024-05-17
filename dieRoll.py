import tkinter as tk
from tkinter import ttk
import random
from collections import Counter

class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")
        self.root.configure(bg='#2E2E2E')  # Set dark background color
        
        # List to store the last 10 rolls
        self.roll_history = []

        # Selected dice type and number of dice
        self.dice_var = tk.StringVar(value="6")
        self.toggle_var = tk.StringVar(value="1")

        # Create custom style
        self.create_styles()
        self.create_widgets()

    def create_styles(self):
        """
        Create custom styles for the widgets.
        """
        style = ttk.Style(self.root)
        style.theme_use('clam')

        # Define custom styles for buttons with rounded corners
        style.configure('TButton',
                        font=('Arial', 10),
                        padding=10,
                        borderwidth=1,
                        relief='flat',
                        focuscolor='',
                        background='#3E3E3E',
                        foreground='white')
        
        style.map('TButton',
                  background=[('active', '#5E5E5E')],
                  foreground=[('active', 'white')])

        # Add specific styles for different dice buttons with rounded corners and brighter colors
        dice_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFC300']
        for idx, color in enumerate(dice_colors, start=1):
            style.configure(f'Dice.TButton.{idx}', background=color, foreground='white', borderwidth=1, relief='flat')
            style.map(f'Dice.TButton.{idx}',
                      background=[('active', '#666666')],
                      foreground=[('active', 'white')])

        # Define custom style for rounded combobox
        style.configure('TCombobox', fieldbackground='#2E2E2E', background='#2E2E2E', foreground='white')
        style.map('TCombobox',
                  fieldbackground=[('readonly', '#2E2E2E')],
                  foreground=[('readonly', 'white')],
                  selectbackground=[('readonly', '#3E3E3E')],
                  selectforeground=[('readonly', 'white')])

        # Define custom style for labels
        style.configure('TLabel', background='#2E2E2E', foreground='white')

    def create_widgets(self):
        """
        Create and arrange widgets in the main window.
        """
        # Label to display the result
        self.label = ttk.Label(self.root, text="Roll the dice!", style='TLabel', font=("Arial", 12))
        self.label.pack(pady=10)

        # Button to roll the dice
        self.roll_button = ttk.Button(self.root, text="Roll Dice", style='TButton', command=self.roll_dice)
        self.roll_button.pack(pady=10)

        # Frame for radio buttons to toggle between one or two dice
        toggle_frame = tk.Frame(self.root, bg='#2E2E2E')
        toggle_frame.pack(pady=5)
        toggle_one = ttk.Radiobutton(toggle_frame, text="One Die", variable=self.toggle_var, value="1", style='TRadiobutton')
        toggle_one.pack(side="left", padx=5)
        toggle_two = ttk.Radiobutton(toggle_frame, text="Two Dice", variable=self.toggle_var, value="2", style='TRadiobutton')
        toggle_two.pack(side="left", padx=5)

        # Label for the dice selector
        dice_selector_label = ttk.Label(self.root, text="Select Dice Type:", style='TLabel', font=("Arial", 10))
        dice_selector_label.pack(pady=(20, 0))

        # Dropdown menu to select the type of dice
        dice_options = [6, 8, 10, 12, 20]
        self.dice_menu = ttk.Combobox(self.root, textvariable=self.dice_var, values=dice_options, state="readonly", style='TCombobox')
        self.dice_menu.pack(pady=10)
        self.dice_menu.set("6")

        # Label for the history combobox
        history_label = ttk.Label(self.root, text="History:", style='TLabel', font=("Arial", 10))
        history_label.pack(pady=(20, 0))

        # Combobox to display the roll history
        self.history_var = tk.StringVar()
        self.history_combobox = ttk.Combobox(self.root, textvariable=self.history_var, state="readonly", style='TCombobox')
        self.history_combobox.pack(pady=10)
        self.update_history_combobox()

        # Label to display the stats
        self.stats_label = ttk.Label(self.root, text="Stats: Most frequent roll:", style='TLabel', font=("Arial", 10))
        self.stats_label.pack(pady=10)

    def roll_dice(self):
        """
        Rolls the dice based on the selected options and updates the result label and history.
        """
        dice_type = int(self.dice_var.get())  # Get the selected dice type (sides)
        num_dice = int(self.toggle_var.get())  # Get the number of dice to roll

        if num_dice == 1:
            roll = random.randint(1, dice_type)
        else:
            roll = random.randint(1, dice_type) + random.randint(1, dice_type)

        # Update the label with the result
        self.label.config(text=f"You rolled a {roll}!")

        # Update the roll history
        self.update_history(roll)

    def update_history(self, roll):
        """
        Updates the roll history list and history combobox with the new roll.
        """
        # Add the new roll to the history list
        self.roll_history.append(roll)

        # Keep only the last 10 rolls
        if len(self.roll_history) > 10:
            self.roll_history.pop(0)

        # Update the history combobox
        self.update_history_combobox()

        # Update the stats
        self.update_stats()

    def update_history_combobox(self):
        """
        Updates the history combobox with the current roll history.
        """
        # Update the values in the combobox
        self.history_combobox['values'] = self.roll_history
        # Set the combobox to display the most recent roll if there are rolls in the history
        if self.roll_history:
            self.history_combobox.current(len(self.roll_history) - 1)

    def update_stats(self):
        """
        Updates the stats label with the most frequently rolled number in the history.
        """
        if self.roll_history:
            # Calculate the frequency of each roll
            roll_counts = Counter(self.roll_history)
            # Find the most common roll(s)
            most_common = roll_counts.most_common(1)[0]
            most_common_roll = most_common[0]
            count = most_common[1]

            # Update the stats label with the most frequent roll and its count
            self.stats_label.config(text=f"Stats: Most frequent roll: {most_common_roll} (rolled {count} times)")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()






