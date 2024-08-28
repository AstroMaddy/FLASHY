from tkinter import *
import random
import pandas as pd
from PIL import Image, ImageDraw, ImageFont


BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#000000"
GREY = "#808080"
WHITE = "#FFFFFF"
current_card = {}
df = pd.DataFrame
current_card = {}



try:
    data_to_display = pd.read_csv("./message.txt")
    oriented_data = df.to_dict(data_to_display, orient="records")
except FileNotFoundError:
    data_to_display = pd.read_csv("./message.txt")
    oriented_data = df.to_dict(data_to_display, orient="records")


def new_card():
    global current_card
    # window.after_cancel(flip_timer)
    current_card = random.choice(oriented_data)
    print(current_card)
    # canvas.itemconfig(upper_text, text="Question", fill="black")
    # canvas.itemconfig(lower_text, text="options", fill="black")
    # canvas.itemconfig(image, image=c_front_img)


# ------------------------- UI DESIGN ----------------------------------------#


# Screen


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.geometry("900x600")
# flip_timer = window.after(3000, func=flip_card)

# BG_Image
canvas = Canvas(width=800, height=600, background=BACKGROUND_COLOR, highlightthickness=0)
c_front_img = PhotoImage(file="./images/card_front.png")
button_img = PhotoImage(file="./Button.png")
# c_back_img = PhotoImage(file="./images/card_back.png")
# question_img = PhotoImage(file="./Question.png")

image = canvas.create_image(400, 260, image=c_front_img)
upper_text = canvas.create_text(400, 75, text='Lorem Epsum. Lorem Epsum. Lorem Epsum. Lorem Epsum.\nLorem Epsum. Lorem Epsum.Lorem Epsum. Lorem Epsum. Lorem Epsum. Lorem Epsum.\nLorem Epsum. Lorem Epsum.Lorem Epsum. Lorem Epsum. Lorem Epsum. Lorem Epsum.\nLorem Epsum. Lorem Epsum.', anchor="center", font=('Ariel', 20, "italic"), fill='Black', width=600, justify="center")
# choice1 = canvas.create_text(180, 250, text="choice1", anchor='center', font=('Ariel', 40, "italic"), fill='Black')
# choice2 = canvas.create_text(600, 250, text="choice2", anchor='center', font=('Ariel', 40, "italic"), fill='Black')
# choice3 = canvas.create_text(180, 400, text="choice3", anchor='center', font=('Ariel', 40, "italic"), fill='Black')
# choice4 = canvas.create_text(600, 400, text="choice4", anchor='center', font=('Ariel', 40, "italic"), fill='Black')
canvas.place(x=5, y=0)

choice1 = Button(image=button_img, width=350, height=100, bg=WHITE, highlightthickness=0, border=0, command=new_card)
choice1.place(x=20, y=200)

choice2 = Button(image=button_img, width=350, height=100, bg=WHITE, highlightthickness=0, border=0, command=new_card)
choice2.place(x=400, y=200)

choice3 = Button(image=button_img, width=350, height=100, bg=WHITE, highlightthickness=0, border=0, command=new_card)
choice3.place(x=20, y=350)

choice4 = Button(image=button_img, width=350, height=100, bg=WHITE,  highlightthickness=0, border=0, command=new_card)
choice4.place(x=400, y=350)

# question_label = Label(image=question_img, bg=WHITE, width=500, height=250)
# question_label.place(x=150, y=60)

new_card()

window.mainloop()
