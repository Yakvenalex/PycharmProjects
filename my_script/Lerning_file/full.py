import pyperclip

def get_entry():
    value = name.get()
    a = f'Здравсвуйте, {value}!\n'
    c = 'Мы российская парфюмерная компания U Project Studio. Хотим подготовить для вас подарок - авторский персональный парфюм. Когда вам понравится,  будем благодарны за небольшое упоминание о нас на Вашей страничке.\n'
    d = 'Если интересно – пишите. Будем рады стараться для вас.'
    insta = a + '⠀\n' + c + '⠀\n' + d
    pyperclip.copy(insta)
    if value:
        label_1['text'] = 'Текст скопирован!'
        label_1['bg'] = 'green'
    else:
        label_1['text'] = 'Вы не ввели имя!'
        label_1['bg'] = 'red'

def del_entry():
    label_1['text'] = 'Тут появится статус'
    label_1['bg'] = 'yellow'
    name.delete(0,tk.END)

import tkinter as tk

win = tk.Tk()

h = 535
w = 117

win.config(bg='#A9FCF3')
win.title('Для инсты')
win.geometry(f'{h}x{w}+100+50')
win.resizable(False,False)
tk.Label(win, text='Введи имя:',font=('Arial',17,'bold'),relief=tk.RAISED).grid(row=0,column=0,stick='we')
name = tk.Entry(win,font=('Arial',17,'normal'),bd=3)
name.grid(row=0,column=1)

tk.Button(win,text='Запустить программу',command=get_entry,font=('Arial',17,'bold'),relief=tk.RAISED,bg='#bdf0bd').grid(row=1,column=0,stick='we')
tk.Button(win,text='Очистить поле ввода',command=del_entry,font=('Arial',17,'bold'),relief=tk.GROOVE,bg='#b3b3b3').grid(row=1,column=1)

label_1 = tk.Label(win, text='Тут появится статус',
                   bg='yellow',
                   fg='black',
                   font=('Arial',17,'bold'),
                   relief=tk.RAISED,
                   justify=tk.LEFT)
label_1.grid(columnspan=2,stick='we')
#win.grid_columnconfigure(0,minsize=100)
#win.grid_columnconfigure(1,minsize=100)

win.mainloop()