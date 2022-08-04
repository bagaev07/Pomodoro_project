from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
label_title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label_title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 130, fill="white", text="00:30", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", font=(FONT_NAME, 12, "bold"))
button_start.grid(column=0, row=2)

button_restart = Button(text="Restart", font=(FONT_NAME,12,"bold"))
button_restart.grid(column=2, row=2)

label_complete = Label(text="✔", font=(FONT_NAME, 24,"bold"), bg=YELLOW, fg=GREEN)
label_complete.grid(column=1, row=3)

window.mainloop()