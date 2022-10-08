import tkinter as tk

MainForm = tk.Tk()
MainForm.title('Aula de Designer com Tkinter')
MainForm.geometry('600x400+50+50')
#MainForm.resizable(False, False)

frame = tk.Frame(MainForm)

altura = 7
largura = 15

button1 = tk.Button(frame,height=altura, width=largura)
button1.grid(row=0, column=0)



frame.grid()
frame.pack(expand=True, side='left')

frame['borderwidth'] = 14

MainForm.mainloop()