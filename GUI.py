# tkinter para fazer a interface gráfica
from tkinter import *
import math
import time

# usamos essa importação para pegar a imagem de
# qualquer pasta em que ela estiver, basta fazer esse
# simples path e conseguimos manusear a imagem com facilidade
import os

def GUI_campo(robo, bola):
    path = os.path.dirname(__file__)
    scale = 1.5
    w = int(900)
    h = int(600)
    pixel_scale = int(100 * scale)

    root = Tk()
    root.title("Ora Bolas")
    root.geometry(f"{w}x{h}+0+0")
    root.maxsize(w, h)
    root.minsize(w, h)
    root.attributes('-topmost', True)
    C = Canvas(root, height=h, width=w)
    imgCampo = PhotoImage(file = path +"\\campo.png")
    l_campo = Label(root,image = imgCampo)
    l_campo.place(x=0,y=0)
    C.pack()



    contador = 0
    while(contador != len(robo["x"])):
        C.delete("all")
        
        x0_robo_pixel = (robo["x"][contador] * pixel_scale) - ((robo["raio"]) * 150)
        y0_robo_pixel = (robo["y"][contador] * pixel_scale) - ((robo["raio"]) * 150)
        x_robo_pixel = (robo["x"][contador] * pixel_scale) + ((robo["raio"]) * 150)
        y_robo_pixel = (robo["y"][contador] * pixel_scale) + ((robo["raio"]) * 150)
        center_robo_pixel = [(robo["x"][contador]* pixel_scale), (robo["y"][contador] * pixel_scale)]

        x0_bola_pixel = (bola["x"][contador] * pixel_scale) - ((bola["raio"]) * 300)
        y0_bola_pixel = (bola["y"][contador] * pixel_scale) - ((bola["raio"])  * 300)
        x_bola_pixel = (bola["x"][contador] * pixel_scale) + ((bola["raio"])  * 300)
        y_bola_pixel = (bola["y"][contador] * pixel_scale) + ((bola["raio"])  * 300)
        center_bola_pixel = [(bola["x"][contador] * pixel_scale), (bola["y"][contador] * pixel_scale)]

        for i in range(0, contador, 2):
            
            draw_robo_path  = C.create_line((robo["x"][i] * pixel_scale), (h - (robo["y"][i] * pixel_scale)), (robo["x"][i + 1] * pixel_scale), (h - (robo["y"][i + 1] * pixel_scale)), fill="black", width=6)
            draw_bola_path  = C.create_line((bola["x"][i] * pixel_scale), (h - (bola["y"][i] * pixel_scale)), (bola["x"][i + 1] * pixel_scale), (h - (bola["y"][i + 1] * pixel_scale)), fill="red", width=6)
            
            draw_robo = C.create_oval(x0_robo_pixel, (h - y0_robo_pixel), x_robo_pixel, (h - y_robo_pixel), fill="black")
            draw_bola = C.create_oval(x0_bola_pixel, (h - y0_bola_pixel), x_bola_pixel, (h - y_bola_pixel), fill="red")

        time.sleep(0.02)
        contador += 1
        C.update()
        

       

    root.mainloop()


