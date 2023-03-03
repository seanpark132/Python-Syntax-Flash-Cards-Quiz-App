import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
LABEL_FONT = ("Ariel", 20, "italic")
TEXT_FONT = ("Ariel", 17, "bold")
SCORE = 0
TOTAL_CARDS = 0
TIME_SECONDS = 30

random_function = {}
timer = None
left_timer = None
button_pressed = False

#  Read CSV Data
data = pandas.read_csv("data/python_functions.csv")
data_dict = data.to_dict(orient="records")


# Choose a random input/output/definition from the data dictionary
def new_card():
    if not data_dict:
        canvas.itemconfig(correct_incorrect_label, text="You have correctly answered \nall the flash cards!", fill="green")
    else:
        global random_function, timer, button_pressed
        button_pressed = False
        window.after_cancel(timer)
        if left_timer is None:
            pass
        else:
            window.after_cancel(left_timer)
        count_down(TIME_SECONDS)
        flip_next_button.config(image=flip_img, command=lambda: [flip_card(), button_on()])
        random_function = random.choice(data_dict)

        canvas.itemconfig(in_out_label, text="Input:", fill="black")
        canvas.itemconfig(card, image=input_card_img)
        canvas.itemconfig(in_out_text, text=random_function["Input"], fill="black")
        canvas.itemconfig(correct_incorrect_label, text="")
        canvas.itemconfig(entry_label, text="What is the output?", fill="black")
        canvas.itemconfig(answer, window=entry)
        canvas.itemconfig(definition_text, text="")
        canvas.itemconfig(definition_label, text="")
        timer = window.after(TIME_SECONDS * 1000, check_flip_button_pressed)
        entry.focus()


def flip_card():
    global TOTAL_CARDS, SCORE
    window.after_cancel(left_timer)
    flip_next_button.config(image=next_img, command=new_card)
    correct_output = random_function["Output"]
    inputted_answer = entry.get()
    answer_text.config(text=inputted_answer)
    TOTAL_CARDS += 1
    if inputted_answer.replace(" ", "") == correct_output.replace(" ", ""):
        SCORE += 1
        canvas.itemconfig(correct_incorrect_label, fill="green", text="CORRECT")
        data_dict.remove(random_function)
    else:
        canvas.itemconfig(correct_incorrect_label, fill="red", text="INCORRECT")
    score_label.config(text=f"Score: {SCORE}/{TOTAL_CARDS}")
    timer_label.config(text="")

    canvas.itemconfig(card, image=output_card_img)
    canvas.itemconfig(in_out_label, text="Correct Output:", fill="white")
    canvas.itemconfig(in_out_text, text=correct_output, fill="white")
    canvas.itemconfig(entry_label, text="Your answer:", fill="white")
    canvas.itemconfig(answer, window=answer_text)
    canvas.itemconfig(definition_label, text="Definition:")
    canvas.itemconfig(definition_text, text=random_function["Definition"])

    entry.delete(0, END)


def check_flip_button_pressed():
    global button_pressed
    if not button_pressed:
        flip_card()


def button_on():
    global button_pressed
    button_pressed = True


def count_down(count):
    timer_label.config(text=f"Time: {count}")
    if count > 0:
        global left_timer
        left_timer = window.after(1000, count_down, count - 1)


# UI SETUP
window = Tk()
window.title("Python Functions Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(TIME_SECONDS * 1000, check_flip_button_pressed)

# CANVAS SETUP
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
input_card_img = PhotoImage(file="images/card_front.png")
output_card_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=input_card_img)
in_out_label = canvas.create_text(400, 60, text="", font=LABEL_FONT)
in_out_text = canvas.create_text(400, 140, text="", font=TEXT_FONT)
correct_incorrect_label = canvas.create_text(400, 220, text="", font=("Ariel", 30, "italic"))
entry_label = canvas.create_text(400, 280, text="", font=LABEL_FONT)
entry = Entry(width=60, highlightthickness=2, highlightcolor="black")
entry.focus()
answer_text = Label(text="", bg="#91c2af", fg="white", font=TEXT_FONT)
answer = canvas.create_window(400, 310, window=entry)
definition_label = canvas.create_text(400, 400, text="",  font=LABEL_FONT)
definition_text = canvas.create_text(400, 430, text="", font=TEXT_FONT)
canvas.grid(column=0, row=0, rowspan=2, padx=(0,20))

# BUTTON SETUP
flip_img = PhotoImage(file="images/flip.png")
next_img = PhotoImage(file="images/next.png")
flip_next_button = Button(bg=BACKGROUND_COLOR, highlightthickness=0, bd= 0)
flip_next_button.grid(column=0, row=2)

# VISUAL TIMER / SCORE SETUP
timer_label = Label(text="Time left: ", bg=BACKGROUND_COLOR, font=("Ariel", 25, "bold"))
timer_label.grid(column=1, row=0, sticky="W")
score_label = Label(text="Score:     ", bg=BACKGROUND_COLOR, font=("Ariel", 25, "bold"))
score_label.grid(column=1, row=1,sticky="W")

new_card()

window.mainloop()
