import tkinter as tk
import random
import json
import os

LEADERBOARD_FILE = 'leaderboard.json'

class LetterMathGame:
    def __init__(self, master):
        self.master = master
        master.title('Letter Math Game')
        self.letters = 'ABCDEFGH'
        self.game_types = {
            'Value': self.letter_value,
            'Sum': self.letter_sum,
            'Difference': self.letter_difference,
            'Product': self.letter_product,
        }
        self.create_main_menu()

    def create_main_menu(self):
        for w in self.master.winfo_children():
            w.destroy()
        tk.Label(self.master, text='Select Game Type:', font=('Arial', 14)).pack(pady=10)
        self.game_var = tk.StringVar(value='Value')
        tk.OptionMenu(self.master, self.game_var, *self.game_types.keys()).pack(pady=5)
        tk.Button(self.master, text='Start Game', command=self.start_game).pack(pady=5)
        tk.Button(self.master, text='View Leaderboard', command=self.show_leaderboard).pack(pady=5)

    def start_game(self):
        self.score = 0
        self.current_streak = 0
        self.longest_streak = 0
        self.questions = 0
        self.setup_game_screen()
        self.next_question()

    def setup_game_screen(self):
        for w in self.master.winfo_children():
            w.destroy()
        # feedback at top right
        self.feedback_label = tk.Label(self.master, text='', font=('Arial', 10))
        self.feedback_label.pack(anchor='ne', padx=10, pady=2)
        # score and streak at top left
        self.score_label = tk.Label(self.master, text='Score: 0', font=('Arial', 12))
        self.score_label.pack(anchor='nw', padx=10)
        self.streak_label = tk.Label(self.master, text='Streak: 0', font=('Arial', 12))
        self.streak_label.pack(anchor='nw', padx=10)
        # question
        self.question_label = tk.Label(self.master, text='', font=('Arial', 16))
        self.question_label.pack(pady=20)
        # entry field
        self.answer_var = tk.StringVar()
        self.answer_var.trace_add('write', self.on_input_change)
        self.entry = tk.Entry(self.master, font=('Arial', 14), textvariable=self.answer_var)
        self.entry.pack()
        self.entry.focus_set()
        # end game
        tk.Button(self.master, text='End Game', command=self.prompt_save_score).pack(pady=10)

    def next_question(self):
        game_fn = self.game_types[self.game_var.get()]
        self.question_text, self.correct_answer = game_fn()
        self.question_label.config(text=self.question_text)
        self.answer_var.set('')
        self.entry.focus_set()

    def on_input_change(self, *args):
        val = self.answer_var.get().strip()
        expected_len = len(str(self.correct_answer))
        if val.isdigit() and len(val) == expected_len:
            self.check_answer()

    def check_answer(self):
        user_input = self.answer_var.get().strip()
        if user_input.isdigit() and int(user_input) == self.correct_answer:
            self.score += 1
            self.current_streak += 1
            if self.current_streak > self.longest_streak:
                self.longest_streak = self.current_streak
            self.feedback_label.config(text='Correct!')
        else:
            self.feedback_label.config(text=f'Wrong! Ans: {self.correct_answer}')
            self.current_streak = 0
        self.questions += 1
        # update displays
        self.score_label.config(text=f'Score: {self.score}')
        self.streak_label.config(text=f'Streak: {self.current_streak}')
        # next question
        self.master.after(200, self.next_question)

    def letter_value(self):
        letter = random.choice(self.letters)
        value = self.letters.index(letter) + 1
        return f'Value of letter {letter}:', value

    def letter_sum(self):
        a, b = random.sample(self.letters, 2)
        total = (self.letters.index(a)+1) + (self.letters.index(b)+1)
        return f'Sum of {a} + {b}:', total

    def letter_difference(self):
        a, b = random.sample(self.letters, 2)
        diff = abs((self.letters.index(a)+1) - (self.letters.index(b)+1))
        return f'Difference of {a} - {b} (abs):', diff

    def letter_product(self):
        a, b = random.sample(self.letters, 2)
        prod = (self.letters.index(a)+1) * (self.letters.index(b)+1)
        return f'Product of {a} * {b}:', prod

    def prompt_save_score(self):
        for w in self.master.winfo_children():
            w.destroy()
        tk.Label(self.master, text=f'Game Over! Score: {self.score}', font=('Arial', 16)).pack(pady=10)
        tk.Label(self.master, text=f'Longest Streak: {self.longest_streak}', font=('Arial', 14)).pack(pady=5)
        tk.Label(self.master, text='Enter your name:').pack(pady=5)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack(pady=5)
        tk.Button(self.master, text='Save Score', command=self.save_score).pack(pady=5)
        tk.Button(self.master, text='Cancel', command=self.create_main_menu).pack(pady=5)

    def save_score(self):
        name = self.name_entry.get().strip() or 'Anonymous'
        data = self.load_leaderboard()
        entry = {'name': name, 'score': self.score, 'longest_streak': self.longest_streak}
        data.setdefault(self.game_var.get(), []).append(entry)
        with open(LEADERBOARD_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        self.create_main_menu()

    def show_leaderboard(self):
        for w in self.master.winfo_children():
            w.destroy()
        tk.Label(self.master, text='Leaderboard', font=('Arial', 16)).pack(pady=10)
        data = self.load_leaderboard()
        scores = data.get(self.game_var.get(), [])
        top = sorted(scores, key=lambda x: x['score'], reverse=True)[:5]
        for entry in top:
            name = entry.get('name')
            sc = entry.get('score', 0)
            ls = entry.get('longest_streak', 0)
            tk.Label(self.master, text=f"{name}: pts {sc}, streak {ls}").pack()
        tk.Button(self.master, text='Back', command=self.create_main_menu).pack(pady=5)

    def load_leaderboard(self):
        if os.path.exists(LEADERBOARD_FILE):
            with open(LEADERBOARD_FILE) as f:
                return json.load(f)
        return {}

if __name__ == '__main__':
    root = tk.Tk()
    app = LetterMathGame(root)
    root.mainloop()
