from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Label
        self.score_label = Label(text=f"Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text((150, 125),
                                                     text="Text",
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Button
        check_img = PhotoImage(file="images/true.png")
        cross_img = PhotoImage(file="images/false.png")
        self.right_button = Button(image=check_img, highlightthickness=0, command=self.true_pressed)
        self.wrong_button = Button(image=cross_img, highlightthickness=0, command=self.false_pressed)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score was: {self.quiz.score}/"
                                                            f"{self.quiz.question_number}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



