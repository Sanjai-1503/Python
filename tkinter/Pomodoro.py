import math
from tkinter import *

work_time = 25
short_break = 5
long_break = 20
reps = 1
start = None

window = Tk()
window.title("Pomodoro")
window.configure(background="lightblue", padx=100, pady=50)


def call_timer():
    global reps
    work_sec = work_time * 60
    short_sec = short_break * 60
    long_sec = long_break * 60

    if reps % 2 == 0 and reps < 8:
        timer(short_sec)
        reps += 1
        rem = reps // 2
        canvas2.itemconfig(heading, fill="red", text="Break")
        button1.configure(bg="red")
        button2.configure(bg="red")
        check_mark.config(text=rem * "☑")
    elif reps % 2 == 1 and reps < 8:
        timer(work_sec)
        reps += 1
        canvas2.itemconfig(heading, fill="green", text="Work")
        button1.configure(bg="green")
        button2.configure(bg="green")
    else:
        timer(long_sec)
        canvas2.itemconfig(heading, fill="darkblue", text="LongBreak")
        button1.configure(bg="darkblue")
        button2.configure(bg="darkblue")
        reps = 1


def reset_button():
    global reps
    window.after_cancel(start)
    canvas.itemconfig(timer_can, text="00:00")
    canvas2.itemconfig(heading, text="TIMER")
    check_mark.config(text="")
    reps = 1


def timer(count):
    mins = math.floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = "0" + str(secs)
    canvas.itemconfig(timer_can, text=f"{mins}:{secs}")
    if count >= 0:
        global start
        start = window.after(1000, timer, count - 1)
    else:
        call_timer()


canvas = Canvas(background="lightblue", width=200, height=224, highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pic)
timer_can = canvas.create_text(100, 130, text="00:00", font=("arial", 35, "bold"))
canvas.grid(column=1, row=1)

canvas2 = Canvas(background="lightblue", width=280, height=50, highlightthickness=0)
heading = canvas2.create_text(140, 23, text="TIMER", font=("arial", 35, "bold"), fill="green")
canvas2.grid(column=1, row=0)

button1 = Button(text="Start", font=("arial", 15, "bold"), command=call_timer)
button1.grid(column=0, row=3)
button1.configure(fg="white", background="green", activebackground="lightblue", activeforeground="black")

button2 = Button(text="Reset", font=("arial", 15, "bold"), command=reset_button)
button2.grid(column=3, row=3)
button2.configure(fg="white", background="green", activebackground="lightblue", activeforeground="black")

check_mark = Label(fg="green", bg="lightblue", font=("arial", 16, "bold"), pady=20)
check_mark.grid(column=1, row=3)
window.mainloop()
