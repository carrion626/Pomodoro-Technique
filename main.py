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
check_plus = '✓'
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(timer)
    global reps
    reps = 0
    timer_label['text'] = 'Timer'
    check_label['text'] = ''
    canvas.itemconfig(text_count, text='00:00')
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 8 == 0:
        count_down(long_sec)
        timer_label['text'] = 'LONG REST'
        timer_label['fg'] = PINK
    elif reps % 2 == 0:
        count_down(short_sec)
        timer_label['text'] = 'REST'
        timer_label['fg'] = PINK
    else:
        count_down(work_sec)
        timer_label['text'] = 'WORK'
        timer_label['fg'] = GREEN


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(counter):

    count_minute = math.floor(counter / 60)
    count_sec = counter % 60
    if count_sec < 10:
        count_sec = '0' + str(count_sec)

    canvas.itemconfig(text_count, text=f'{count_minute}:{count_sec}')
    if counter > 0:
        global timer
        timer = window.after(1000, count_down, counter - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark = ''
            work_sessions = (math.floor(reps/2))
            for _ in range(work_sessions):
                mark += '✓'
            check_label['text'] = mark


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('POMODORO')
window.config(padx=100, pady=50, bg=(YELLOW))

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
text_count = canvas.create_text(103, 140, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# count_down(5)

timer_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', bg=YELLOW, fg='blue', font=(FONT_NAME, 14), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', bg=YELLOW, fg='blue', font=(FONT_NAME, 14), highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_label = Label(text='', font=(FONT_NAME, 25, 'bold'), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)



window.mainloop()
