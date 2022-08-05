from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    label_title.config(text="Timer")
    canvas.itemconfig(text_count, text="00:00")
    label_complete.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 5
    long_break_min = LONG_BREAK_MIN * 5

    if reps % 8 == 0:
        count_down(long_break_min)
        label_title.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_min)
        label_title.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_min)
        label_title.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(text_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        label_complete.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
label_title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label_title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_count = canvas.create_text(103, 130, fill="white", text="00:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


button_start = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
button_start.grid(column=0, row=2)

button_restart = Button(text="Restart", font=(FONT_NAME,12,"bold"), command=reset_timer)
button_restart.grid(column=2, row=2)

label_complete = Label(font=(FONT_NAME, 24,"bold"), bg=YELLOW, fg=GREEN)
label_complete.grid(column=1, row=3)

window.mainloop()