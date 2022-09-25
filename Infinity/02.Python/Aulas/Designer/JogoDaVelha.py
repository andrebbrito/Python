import tkinter as tk

MainForm = tk.Tk()
MainForm.title('Aula de Designer com Tkinter')
MainForm.geometry('600x400+50+50')
MainForm.resizable(False, False)

frame = tk.Frame(MainForm)

altura = 7
largura = 15

button1 = tk.Button(frame,height=altura, width=largura)
button2 = tk.Button(frame,height=altura, width=largura)
button3 = tk.Button(frame,height=altura, width=largura)
button4 = tk.Button(frame,height=altura, width=largura)
button5 = tk.Button(frame,height=altura, width=largura)
button6 = tk.Button(frame,height=altura, width=largura)
button7 = tk.Button(frame,height=altura, width=largura)
button8 = tk.Button(frame,height=altura, width=largura)
button9 = tk.Button(frame,height=altura, width=largura)

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
button4.grid(row=0, column=1)
button5.grid(row=1, column=1)
button6.grid(row=2, column=1)
button7.grid(row=0, column=2)
button8.grid(row=1, column=2)
button9.grid(row=2, column=2)

button10 = tk.Button(frame,height=3, width=4)
button11 = tk.Button(frame,height=3, width=4)

button10.grid(row=0, column=4)
button11.grid(row=0, column=4)

frame.grid()
frame.pack(side='left')


MainForm.mainloop()
