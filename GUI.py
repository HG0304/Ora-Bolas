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
    w = int(900 * scale)
    h = int(600 * scale)
    pixel_scale = int(100 * scale)
    vector_scale = float(1 / 5)

    root = Tk()
    root.title("Ora Bolas")
    root.geometry("{}x{}+0+0".format(w, h))
    root.maxsize(w, h)
    root.minsize(w, h)
    root.attributes('-topmost', True)

    C = Canvas(root, height=h, width=w)

    for cont_interface in range(len(robo["x"])):
        C.delete("all")
        C.config(bg="#306324")
        C.pack()

        robo_x_scaled = robo["x"][cont_interface] * pixel_scale
        robo_y_scaled = robo["y"][cont_interface] * pixel_scale
        bola_x_scaled = bola["x"][cont_interface] * pixel_scale
        bola_y_scaled = bola["y"][cont_interface] * pixel_scale

        robo_raio_scaled = robo["raio"] * scale
        bola_raio_scaled = bola["raio"] * scale

        x0_robo_pixel = robo_x_scaled - robo_raio_scaled
        y0_robo_pixel = robo_y_scaled - robo_raio_scaled
        x_robo_pixel = robo_x_scaled + robo_raio_scaled
        y_robo_pixel = robo_y_scaled + robo_raio_scaled

        x0_bola_pixel = bola_x_scaled - bola_raio_scaled
        y0_bola_pixel = bola_y_scaled - bola_raio_scaled
        x_bola_pixel = bola_x_scaled + bola_raio_scaled
        y_bola_pixel = bola_y_scaled + bola_raio_scaled

         # Criação dos objetos gráficos para o robô e a bola
        robo_graphic = None
        bola_graphic = None

        for cont_interface in range(len(robo["x"])):
            C.delete("all")
            C.config(bg="#306324")
            C.pack()

            # ... (código anterior)

            # Desenha o robô
            if robo_graphic is not None:
                C.delete(robo_graphic)
            robo_graphic = C.create_oval(x0_robo_pixel, y0_robo_pixel, x_robo_pixel, y_robo_pixel, fill="#F00")

            # Desenha a bola
            if bola_graphic is not None:
                C.delete(bola_graphic)
            bola_graphic = C.create_oval(x0_bola_pixel, y0_bola_pixel, x_bola_pixel, y_bola_pixel, fill="#00F")
        
        # Draw the robot
        C.create_oval(x0_robo_pixel, y0_robo_pixel, x_robo_pixel, y_robo_pixel, fill="#F00")

        # Draw the ball
        C.create_oval(x0_bola_pixel, y0_bola_pixel, x_bola_pixel, y_bola_pixel, fill="#00F")

        # Draw the field
        C.create_rectangle(0, 0, w, h, fill="#306324")
        C.create_line(0, h / 2, w, h / 2, fill="#FFF")
        C.create_line(w / 2, 0, w / 2, h, fill="#FFF")

        # Update the canvas
        root.update()

        # Delay for the next frame
        time.sleep(0.01)

    root.mainloop()


