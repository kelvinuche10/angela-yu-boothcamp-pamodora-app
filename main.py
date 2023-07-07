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
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
	window.after_cancel(timer)
	canvas.itemconfig(timer_canvas, text='00:00')
	timer_label.config(text='Timer', fg=GREEN)
	checkmarks_label.config(text='')
	global reps
	reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	global reps
	reps+=1
	work_sec = WORK_MIN
	short_break_sec = SHORT_BREAK_MIN
	long_break_min = LONG_BREAK_MIN
	
	if reps % 8 == 0:
		count_down(long_break_min)
		timer_label.config(text='Long Break', fg=RED)
	elif reps % 2 == 0:
		count_down(short_break_sec)
		timer_label.config(text='Short Break', fg=PINK)
	else:
		count_down(work_sec)
		timer_label.config(text='Work Time', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
	global reps

	count_min = math.floor(count / 60)
	count_sec = count % 60

	if count_sec == 0:
		count_sec = '00'
	elif count_sec < 10:
		count_sec = f'0{count_sec}'

	canvas.itemconfig(timer_canvas, text=f'{count_min}:{count_sec}')
	if count > 0:
		global timer
		timer = window.after(1000, count_down, count - 1)
	else:
		start_timer()
		marks = ''
		work_sessions = math.floor(reps/2)
		for _ in range(work_sessions):
			marks += '✔'

		checkmarks_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pamodora')
window.config(padx=100, pady=100, bg=YELLOW)

timer_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato_img)
timer_canvas = canvas.create_text(100, 133, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

back = Button(text='Start',bg=YELLOW, command=start_timer)
back.grid(column=0, row=2) 

checkmarks_label = Label(font=(FONT_NAME, 15, 'bold'), fg=GREEN)
checkmarks_label.grid(column=1, row=3)

reset = Button(text='Reset', bg=YELLOW, command=reset)
reset.grid(column=2, row=2)



window.mainloop()