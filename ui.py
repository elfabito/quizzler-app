from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")
class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="", font=FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        img_true = PhotoImage(file="images/true.png")

        self.true_button = Button( image= img_true, highlightthickness=0, command=self.check_true )
        self.true_button.grid(column=0, row=2)
        img_false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=img_false, highlightthickness=0, command=self.check_false )
        self.false_button.grid(column=1, row=2)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz.\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def check_true(self):
        answer = "True"
        self.give_feedback(self.quiz.check_answer(answer))

    def check_false(self):
        answer = "False"
        ans = self.quiz.check_answer(answer)
        self.give_feedback(ans)


    def give_feedback(self, ans):
        if ans:
            self.canvas.config(bg="green")
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_q)
