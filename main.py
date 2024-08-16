from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer1 = None


def check_progress():
    if reps % 8 == 1:
        check.config(text="● ○ ○ ○", fg = GREEN)
    elif reps % 8 == 3:
        check.config(text="● ● ○ ○", fg = GREEN)
    elif reps % 8 == 5:
        check.config(text="● ● ● ○", fg = GREEN)
    elif reps % 8 == 7:
        check.config(text="● ● ● ●", fg = GREEN)
    elif reps % 8 == 0:
        check.config(text="○ ○ ○ ○", fg = GREEN)

# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global reps
    reps = 0
    window.after_cancel(timer1)
    timer.config(text = "Timer", fg = PINK)
    canvas.itemconfig(time, text = "00:00")
    check.config(text="○ ○ ○ ○", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps+= 1
    check_progress()

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text = "Take a Break", fg = PINK)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Take a Breather", fg = PINK)
    elif reps % 2 == 1:
        countdown(work_sec)
        timer.config(text="Time to Grind", fg = RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer1
        timer1 = window.after(1000, countdown, count - 1)
    else:
        start_time()



# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)
window.after(1000)

#Tomato
canvas = Canvas(width = 400, height = 400, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(200, 200, image = tomato_img)
time = canvas.create_text(200, 225, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

#Label
timer = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 40, "bold"))
timer.grid(column = 1, row = 0)

check = Label(text = "○ ○ ○ ○", bg = YELLOW, fg = GREEN)
check.grid(column = 1, row = 3)

#Button

start = Button(text = "Start", highlightbackground = YELLOW, command = start_time)
start.grid(column = 0, row = 2)

reset = Button(text = "Reset", highlightbackground = YELLOW, command = reset)
reset.grid(column = 2, row = 2)




window.mainloop()