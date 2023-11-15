# tkinter para fazer a interface gráfica
from tkinter import *

# usamos essa importação para pegar a imagem de
# qualquer pasta em que ela estiver, basta fazer esse
# simples path e conseguimos manusear a imagem com facilidade
import os

path = os.path.dirname(__file__)

# referente ao posicionamento da imagem e da janela
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


root.mainloop()