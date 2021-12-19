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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def resetTimer():
    screen.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    label.config(text="Timer")
    labelCheck.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countDown(long)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countDown(short)
        label.config(text="Break", fg=PINK)
    else:
        countDown(work)
        label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    second = count % 60
    if second < 10:
        second = f"0{second}"

    minute = count // 60
    if minute < 10:
        minute = f"0{minute}"

    timeNow = f"{minute}:{second}"
    canvas.itemconfig(timerText, text=timeNow)
    if count > 0:
        global timer
        timer = screen.after(1000, countDown, count - 1)
    else:
        startTimer()
        check = "✔"*(reps // 2)
        labelCheck.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro Timer")
screen.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=234, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timerText = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 20, "bold"), fill="White")
canvas.grid(column=1, row=1)

buttonStart = Button(text="Start", command=startTimer)
buttonStart.grid(column=0, row=2)

buttonReset = Button(text="Reset", command=resetTimer)
buttonReset.grid(column=2, row=2)

labelCheck = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
labelCheck.grid(column=1, row=3)

screen.mainloop()
