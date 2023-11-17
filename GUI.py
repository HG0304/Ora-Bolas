# tkinter para fazer a interface gráfica
from tkinter import *
import math
import time

# usamos essa importação para pegar a imagem de
# qualquer pasta em que ela estiver, basta fazer esse
# simples path e conseguimos manusear a imagem com facilidade
import os

def GUI_campo(robo, bola):
    
    scale = 1.5
    w = int(900 * scale)
    h = int(600 * scale)
    pixel_scale = int(100 * scale)

    root = Tk()
    root.title("Ora Bolas")
    root.geometry("{}x{}+0+0".format(w, h))
    root.maxsize(w, h)
    root.minsize(w, h)
    path = os.path.dirname(__file__)
    root.attributes('-topmost', True)
    C = Canvas(root, height=h, width=w)
    # Draw the field
    C.create_rectangle(0, 0, w, h, fill="#306324")
    C.create_line(0, h / 2, w, h / 2, fill="#FFF")
    C.create_line(w / 2, 0, w / 2, h, fill="#FFF")


    contador = 0
    while(contador != len(robo["x"])):
        C.delete("all")
        imgCampo = PhotoImage(file = path +"\\campo.png")
        l_campo = Label(root,image = imgCampo)
        l_campo.place(x=0,y=0)
        C.pack()

        x0_robo_pixel = (robo["x"][contador] * pixel_scale) - ((robo["raio"]) * scale)
        y0_robo_pixel = (robo["y"][contador] * pixel_scale) - ((robo["raio"]) * scale)
        x_robo_pixel = (robo["x"][contador] * pixel_scale) + ((robo["raio"]) * scale)
        y_robo_pixel = (robo["y"][contador] * pixel_scale) + ((robo["raio"]) * scale)
        center_robo_pixel = [(robo["x"][contador]* pixel_scale), (robo["y"][contador] * pixel_scale)]

        x0_bola_pixel = (bola["x"][contador] * pixel_scale) - ((bola["raio"]) * scale)
        y0_bola_pixel = (bola["y"][contador] * pixel_scale) - ((bola["raio"])  * scale)
        x_bola_pixel = (bola["x"][contador] * pixel_scale) + ((bola["raio"])  * scale)
        y_bola_pixel = (bola["y"][contador] * pixel_scale) + ((bola["raio"])  * scale)
        center_bola_pixel = [(bola["x"][contador] * pixel_scale), (bola["y"][contador] * pixel_scale)]

        for i in range(0, contador, 2):
            draw_robo_path = line = C.create_line((robo["x"][i] * pixel_scale), (h - (robo["y"][i] * pixel_scale)), (robo["x"][i + 1] * pixel_scale), (h - (robo["y"][i + 1] * pixel_scale)), fill="#333333", width=4)
            draw_bola_path = line = C.create_line((bola["x"][i] * pixel_scale), (h - (bola["y"][i] * pixel_scale)), (bola["x"][i + 1] * pixel_scale), (h - (bola["y"][i + 1] * pixel_scale)), fill="#bbbbbb", width=4)
            
            draw_robo = C.create_oval(x0_robo_pixel, (h - y0_robo_pixel), x_robo_pixel, (h - y_robo_pixel), fill="black")
            draw_bola = C.create_oval(x0_bola_pixel, (h - y0_bola_pixel), x_bola_pixel, (h - y_bola_pixel), fill="red")

        C.update()
        contador += 1

        # Delay for the next frame
        time.sleep(0.01)

    root.mainloop()


