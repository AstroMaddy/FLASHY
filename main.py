from tkinter import *
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
df = pd.DataFrame
current_card = {}

try:
    data_to_display = pd.read_csv("./data/words_to_learn.csv")
    oriented_data = df.to_dict(data_to_display, orient="records")
except FileNotFoundError:
    data_to_display = pd.read_csv("./data/french_words.csv")
    oriented_data = df.to_dict(data_to_display, orient="records")


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(oriented_data)
    canvas.itemconfig(upper_text, text="French", fill="black")
    canvas.itemconfig(lower_text, text=current_card["French"], fill="black")
    canvas.itemconfig(image, image=c_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(image, image=c_back_img)
    canvas.itemconfig(lower_text, text=current_card["English"], fill="white")
    canvas.itemconfig(upper_text, text='English', fill="white")


def is_known():
    oriented_data.remove(current_card)
    print(len(oriented_data))
    data = pd.DataFrame(oriented_data)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()
# ------------------------- UI DESIGN ----------------------------------------#


# Screen
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# BG_Image
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
c_front_img = PhotoImage(file="./images/card_front.png")
c_back_img = PhotoImage(file="./images/card_back.png")
image = canvas.create_image(400, 260, image=c_front_img)
upper_text = canvas.create_text(400, 150, text='', anchor="center", font=('Ariel', 40, "italic"), fill='Black')
lower_text = canvas.create_text(400, 263, text="", anchor='center', font=('Ariel', 60, "bold"), fill='Black')
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=new_card)
wrong_button.grid(row=1, column=0)

correct_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=is_known)
correct_button.grid(row=1, column=1)

new_card()

window.mainloop()
