# tkinter para fazer a interface gráfica
from tkinter import *
import time

# usamos essa importação para pegar a imagem de
# qualquer pasta em que ela estiver, basta fazer esse
# simples path e conseguimos manusear a imagem com facilidade
import os

def GUI_campo(robo,bola):
    path = os.path.dirname(__file__)

    high = int(900*1.2)
    large = int(600*1.2)
    root = Tk()
    root.title("___Ora Bolas___")
    root.geometry(f"{high}x{large}")
    root.maxsize(f"{high}",f"{large}")
    root.minsize(f"{high}",f"{large}")
    imgCampo = PhotoImage(file = path +"\\campo.png")
    l_campo = Label(root,image = imgCampo)
    l_campo.place(x=80,y=55)
    
    # criando um canvas
    canvas = Canvas(root,width=high, height=large)
    canvas.pack
    
    # criando a bola e o robo
    bola = canvas.create_oval(70,70,70,70, fill="blue")
    robo = canvas.create_rectangle(120,120,120,120, fill="black")
    
    for i in range(len(robo["t"])):
        

     
    root.mainloop()
