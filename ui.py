from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzier")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # LABELS
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, 'normal'))
        self.score_label.grid(column=1, row=0)
        self.check_label = Label(text="", bg=THEME_COLOR, font=("Arial", 15, 'bold'))
        self.check_label.grid(column=0, row=2, columnspan=2)

        # CANVAS SET-UP
        self.canvas = Canvas(width=300, height=250,bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=300, text="Amazon acquared Twitch in August 2014 for $970 million dollars.", font=("Arial", 15, "italic"))
        self.final_score = self.canvas.create_text(150, 195,text="", font=("Arial", 12, "bold"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        # BUTTONS
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(column=1, row=3, pady=30)
        self.false_button.grid(column=0, row=3)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        self.check_label.config(text="")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.canvas.itemconfig(self.final_score, text=f"Final score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def true_pressed(self):
        self.is_right = self.quiz.check_answer("True")
        self.give_feedback(self.is_right)


    def false_pressed(self):
        self.is_right = self.quiz.check_answer("False")
        self.give_feedback(self.is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.check_label.config(text="Correct!", fg="#9af843")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
            self.check_label.config(text="Incorrect!", fg="red")

        self.timer = self.window.after(1000, func=self.get_next_question)
