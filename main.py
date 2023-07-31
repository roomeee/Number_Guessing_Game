from random import randint
import customtkinter as ctk
from tkinter import *

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

class NumberGuessingGame:
    def __init__(self):
        self.num = None
        self.attempts = 0
        self.best_score = float('inf')

        self.root = ctk.CTk()
        self.root.title("Number Guessing Game")
        self.root.geometry('500x500')
        self.root.configure()

        self.label = ctk.CTkLabel(self.root, text='PICK A NUMBER B/W 1-10 ', font=('Arial', 30, 'bold'), text_color='#996ad9')
        self.label.pack(pady=30)

        self.attempts_label = ctk.CTkLabel(self.root, text='Attempts: 0', font=('Arial', 20))
        self.attempts_label.pack()

        self.entry = ctk.CTkEntry(self.root, width=140, height=140, border_width=1, placeholder_text="Enter a number",
                                  text_color='black', font=('Arial', 50))
        self.entry.pack(pady=20)

        self.submit_button = ctk.CTkButton(self.root, text="Submit Guess", command=self.guess_num, fg_color='#996ad9')
        self.submit_button.pack(pady=20)

        self.random_button = ctk.CTkButton(self.root, text="↺", fg_color='red', width=40, height=40,
                                           corner_radius=1, command=self.random_num)
        self.random_button.place(relx=0.99, rely=0.01, anchor='ne')

        self.random_num()
        self.root.mainloop()

    def guess_num(self):
        if self.entry.get().isdigit():
            guess = int(self.entry.get())
            self.attempts += 1
            self.attempts_label.configure(text=f'Attempts: {self.attempts}')

            diff = abs(self.num - guess)

            if guess == self.num:
                self.root.configure(fg_color="SystemButtonFace")
                self.label.configure(text='Correct!', text_color='red')

                if self.attempts < self.best_score:
                    self.best_score = self.attempts

            elif diff == 5:
                bc = '#d0c5e0'
                self.root.configure(fg_color=bc)
                self.label.configure(bg_color=bc)

            elif diff < 5:
                bc = f'#ff{diff}{diff}{diff}{diff}'
                self.root.configure(fg_color=bc)
                self.label.configure(bg_color=bc, text_color='white')
                self.label.configure(text='Getting closer...')

            else:
                bc = f'#{diff}{diff}{diff}{diff}ff'
                self.root.configure(fg_color=bc)
                self.label.configure(bg_color=bc, text_color='white')
                self.label.configure(text='Too far!')

        else:
            self.entry.delete(0, END)
            self.label.configure(text='Type a number please')

    def random_num(self):
        self.num = randint(1, 10)
        self.attempts = 0
        self.attempts_label.configure(text='Attempts: 0')
        self.label.configure(text='PICK A NUMBER B/W 1-10 ')
        self.entry.delete(0, END)
        self.label.configure(bg_color="SystemButtonFace")
        self.root.configure(fg_color="SystemButtonFace")


if __name__ == "__main__":
    NumberGuessingGame()
