import tkinter as tk

janela = tk.Tk()
janela.title('Aula de Designer com Tkinter')
janela.geometry('600x400+50+50')
janela.attributes('-alpha',1)

janela.resizable(False, False)
    

# exit button
exit_button = tk.Button(
    janela,
    text='Download', 
    compound=tk.LEFT,   
    command=lambda: janela.quit()
)

exit_button.pack(
    ipadx=50,
    ipady=50,        
    side='top'
)

def mudarNome():
    exit_button['text'] = 'Mudei'
    print(type(exit_button))      

# Mudar Nome
button = tk.Button(
    janela,
    text='Mudar Botao', 
    command=mudarNome
)

button.pack(
    ipadx=50,
    ipady=50,        
    side='top'
)




janela.mainloop()

