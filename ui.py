from tkinter import *

from setuptools import Command
from quiz_brain import QuizBrain
from numpy import true_divide
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz:QuizBrain) -> None:
        self.quiz=quiz
        self.windows=Tk()
        self.windows.title("Quizller")
        self.windows.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label=Label(text="score:0",fg="white",bg=THEME_COLOR,font=("Arail",20,"bold"))
        self.score_label.grid(column=1,row=0)
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,width=280,text="Your text goes down here.",font=("Arail",12,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
        #creating buttons.
        true_image=PhotoImage(file="images/true.png")
        false_image=PhotoImage(file="images/false.png")
        self.true_button=Button(image=true_image,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)
        self.false_button=Button(image=false_image,command=self.false_pressed)
        self.false_button.grid(row=2,column=1)
        self.next_question()
        self.windows.mainloop()
        
    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000, self.next_question)

