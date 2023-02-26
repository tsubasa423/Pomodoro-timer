from tkinter import *
import tkinter as tk
import math
import winsound

COLOR = '#faefe1'
Font_name = 'Courier'
BREAK_timer = 5
WORK_timer = 25
user = 0
timer = ''

root = Tk()
root.title('ポモドーロタイマー')
root.geometry('510x370')
root.config(background=COLOR)

# スタート
def start_timer():
    global user, timer
    start_btn['state'] = DISABLED

    user += 1
    print(user)

    if user % 2 == 0: 
        shor_break_sec = BREAK_timer * 60
        title_label.config(text=' 休憩タイム!', background=COLOR,
                           foreground='#5c5f66', font=(Font_name, 40, 'bold'))
        count_down(shor_break_sec)
    else:
        title_label.config(text=' 仕事に集中！', background=COLOR,
                           foreground='#5c5f66', font=(Font_name, 40, 'bold'))
        worker_sec = WORK_timer * 60
        count_down(worker_sec)     

# リセット
def reset_timer():
    global user, timer

    root.after_cancel(timer)
    fix_posi.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', background=COLOR,
                       foreground='#5c5f66', font=(Font_name, 40, 'bold'))
    user = 0
    start_btn['state'] = NORMAL

# カウントダウン
def count_down(count):
    global user, timer
    counter_min = math.floor(count/60)
    counter_sec = count % 60

    if counter_sec < 10:
        counter_sec = f'0{counter_sec}'

    fix_posi.itemconfig(timer_text, text=f'{counter_min}:{counter_sec}')
    if count > 0:
        timer = root.after(1000, count_down, count-1)
    else:
        start_timer()
        winsound.Beep(1000, 900) #時間お知らせ
# ラベル設定
title_label = tk.Label(text='Timer', background=COLOR,
                        foreground='#5c5f66', font=(Font_name, 40, 'bold'))
title_label.grid(column=1, row=0,pady=20)

# Canvas セット
fix_posi = Canvas(width=512, height=515, background=COLOR, highlightthickness=0)
timer_text = fix_posi.create_text(
    256, 60, text='00:00', fill='#5c5f66', font=(Font_name, 50, 'bold'))
fix_posi.grid(column=1, row=1)

# ボタン設定
start_btn = tk.Button(text='Start',command=start_timer,font=('Courier',16,'bold'))
start_btn.place(x=100,y=250,height=70,width=130)

reset_btn = tk.Button(text='Reset', command=reset_timer,font=('Courier',16,'bold'))
reset_btn.place(x=280,y=250,height=70,width=130)

root.mainloop()