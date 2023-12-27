from tkinter import *
from quiz_brain import QuizBrain
from data import question_data

THEME_COLOR = "#375362"
FONT_QUESTION = ("Arial", 18, "italic")
FONT_SCORE = ("Arial", 12, "bold")
class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.timer = None
        self.score = 0

        # Window Setup
        self.window = Tk()
        self.window.title("Geek Quiz")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.window.resizable(False, False)

        # Images
        self.true = PhotoImage(file="images/true.png")
        self.false = PhotoImage(file="images/false.png")

        # Labels
        self.score_label = Label(text=f"Score: {self.score}/{len(question_data)}",
                                 background=THEME_COLOR,
                                 font=FONT_SCORE,
                                 fg='white'
                                 )
        self.score_label.grid(column=1, row=0)


        # Buttons
        self.true_button = Button(image=self.true,
                                  background="#375362",
                                  highlightthickness=0,
                                  borderwidth=0,
                                  command=self.check_if_true
                                  )

        self.false_button = Button(image=self.false,
                                   background="#375362",
                                   highlightthickness=0,
                                   borderwidth=0,
                                   command=self.check_if_false
                                   )

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        # Canvas
        self.canvas = Canvas(width=300, height=250, background='white', highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=290,
            text="This will be a question",
            font=FONT_QUESTION)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.true_button["state"] = "normal"
        self.false_button["state"] = "normal"
        self.canvas.config(background='white')
        try:
            q_text = self.quiz.next_question()
        except IndexError:
            self.canvas.itemconfig(self.question_text, text=f"Your score is: {self.score}/10\n\n"
                                                            "Restart for more questions!", fill='black', justify='center')
            self.score_label.destroy()
            self.true_button.destroy()
            self.false_button.destroy()
        else:
            self.canvas.itemconfig(self.question_text, text=q_text, fill='black')

    def check_if_true(self):
        if self.quiz.check_answer("True"):
            self.notify('Correct')
        else:
            self.notify('Incorrect')

    def check_if_false(self):
        if self.quiz.check_answer("False"):
            self.notify("Correct")
        else:
            self.notify('Incorrect')

    def notify(self, result):
        self.true_button["state"] = "disabled"
        self.false_button["state"] = "disabled"
        if result == 'Correct':
            self.canvas.config(background="green")
            self.canvas.itemconfig(self.question_text, fill='white')
            self.score += 1
            self.score_label['text'] = f"Score: {self.score}/{len(question_data)}"
        else:
            self.canvas.config(background="red")
            self.canvas.itemconfig(self.question_text, fill='white')

        self.timer = self.window.after(1500, self.get_next_question)
