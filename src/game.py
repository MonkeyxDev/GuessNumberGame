from ui import GuessNumberUi,OkMessage
import random
import customtkinter as ctk

class GuessNumberGame:
    def __init__(self, ui):
        self.ui = ui
        self.secret = random.randint(1, 100)
        self.chance = 20
        self.try_number = 0
        self.difficulty = "Easy"
        self.Hint_State = "on"
        self.ui.guess_btn.configure(command=self.check_guess)
        self.ui.newgame_btn.configure(command=self.new_game)
        self.ui.exit_btn.configure(command=self.exit_app)
        self.ui.difficulty_segment.configure(command=self.on_difficulty_change)
        self.ui.btn_dark.configure(command=lambda: self.change_theme("Dark"))
        self.ui.btn_light.configure(command=lambda: self.change_theme("Light"))
        self.ui.hint_var.trace_add("write", self.toggle_hint)

    def check_guess(self):
        try:
            guess = int(self.ui.guess_entry.get())
        except ValueError:
            OkMessage(self.ui, "Error", "Enter a Number")
            return
        self.chance -= 1
        self.try_number +=1
        self.ui.count_label.configure(text=f"You Have {self.chance} Chance To Guess")
        if guess == self.secret:
            OkMessage(self.ui, "Win", f"Congratulations, You Won! \n Number of tries: {self.try_number}")
            self.ui.guess_btn.configure(state="disabled")
            self.ui.hint_label.pack_forget()
        elif guess < self.secret:
            self.ui.hint_label.configure(text="Higher!")
        elif guess > self.secret:
            self.ui.hint_label.configure(text="Lower!")
        if self.chance <= 0:
            OkMessage(self.ui, "Lose", f"You Lose! \n The Number Was: {self.secret}" )
            self.ui.guess_btn.configure(state="disabled")
            self.ui.hint_label.pack_forget()

    def check_difficulty(self):
        if self.difficulty == "Easy":
            self.chance = 20
        elif self.difficulty == "Normal":
            self.chance = 15
        elif self.difficulty == "Hard":
            self.chance = 7

    def new_game(self):
        self.check_difficulty()
        self.secret = random.randint(1, 100)
        self.ui.guess_entry.delete(0, "end")
        self.ui.guess_btn.configure(state="normal")
        self.ui.count_label.configure(text=f"You Have {self.chance} Chance To Guess")
        self.ui.hint_label.configure(text="Guess It? Im Waiting...  ")
        OkMessage(self.ui, "New", "New game started \n Guess Number Changed")
        self.update_hint_display()

    def on_difficulty_change(self, value):
        self.difficulty = value
        self.check_difficulty()
        self.secret = random.randint(1, 100)
        self.ui.guess_entry.delete(0, "end")
        self.ui.guess_btn.configure(state="normal")
        self.ui.count_label.configure(text=f"You Have {self.chance} Chance To Guess")
        self.ui.my_status.configure(text=f"Updated to:   Hints are {self.Hint_State} / Difficulty is on {self.difficulty} ")

        self.update_hint_display()

    def update_hint_display(self):
        if self.ui.hint_var.get() == "on":
            if not self.ui.hint_label.winfo_ismapped():
                self.ui.hint_label.pack(before=self.ui.frame_btn_game)
        else:
            if self.ui.hint_label.winfo_ismapped():
                self.ui.hint_label.pack_forget()

    def toggle_hint(self, *args):
        if self.ui.hint_var.get() == "on":
            self.Hint_State = "on"
            self.ui.my_status.configure(text=f"Updated to:   Hints are {self.Hint_State} / Difficulty is on {self.difficulty} ")
        else:
            self.Hint_State = "off"
            self.ui.my_status.configure(text=f"Updated to:   Hints are {self.Hint_State} / Difficulty is on {self.difficulty} ")
        self.update_hint_display()

    def change_theme(self, mode):
        ctk.set_appearance_mode(mode)

    def exit_app(self):
        self.ui.destroy()
if __name__ == '__main__':
    ui = GuessNumberUi()
    game = GuessNumberGame(ui)
    ui.mainloop()
