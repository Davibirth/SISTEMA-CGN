

import time
from tkinter import *
from tkinter import Tk


menu = Tk()
menu.geometry('750x190')
imagem = PhotoImage(file =r"C:\Users\katia\Downloads\Logo-marca-CGN (4).png")
menu.configure(bg='white')


def verificar():
    dado = caixa2.get()
    dado2 = caixa3.get()
    

def login2():
    global menu3
    menu3  = Tk()
    menu3.title('LOGIN')
    menu3.geometry('200x200')
    menu3.configure(bg = 'white')
    login1 = Label(menu3,text='LOGIN',font=('arial black',15))
    senha = Label(menu3,text='SENHA',font=('arial black',15))
    global caixa2
    global caixa3
    caixa2 = Entry(menu3,width=12,bd = 2,justify='left')
    caixa3 = Entry(menu3,width=12,bd = 2,justify='left')
    login1.grid(column=2,row=0)
    caixa2.grid(column=2,row=1)
    senha.grid(column=2,row=2)
    caixa3.grid(column=2,row=3)
    botao = Button(menu3,text='ENVIAR',command=verificar)
    botao.grid(column=2,row=4)
    menu3.mainloop()

def destruir():
    menu.destroy()
    
def janela():
    menu2 = Tk()
    menu2.title('Sistema Escolar')
    dados = Label(menu2,text='Dados',font=('arial',12))
    caixadetexto1 = Entry(menu2, width=15,bd = 2,justify='left')
    caixadetexto2 = Entry(menu2, width=15,bd = 2,justify='left')
    caixadetexto3 = Entry(menu2, width=15,bd = 2,justify='left')
    dados.grid(column=0,row=0)
    caixadetexto1.grid(column=1,row=1)
    caixadetexto2.grid(column=1,row=1)
    caixadetexto3.grid(column=1,row=1)
    
    menu2.mainloop()   


def func():
    login2()



escondasenha = StringVar

imagem1 = Label(menu,image=imagem)
imagem1.grid(column=0,row=0)
botao = Button(menu,text='login',font=('arial black',15),command=func)
botao.grid(column=1,row=0)
botao2 = Button(menu,text='Registrar',font=('arial black',15),command=func)
botao2.grid(column = 1,row=1)

menu.mainloop()





