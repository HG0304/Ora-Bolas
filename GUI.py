# tkinter para fazer a interface gráfica
from tkinter import *
import math
import time

# usamos essa importação para pegar a imagem de
# qualquer pasta em que ela estiver, basta fazer esse
# simples path e conseguimos manusear a imagem com facilidade
import os

def GUI_campo(robo,bola):
    path = os.path.dirname(__file__)

    # high = int(900*1.2)
    # large = int(600*1.2)
    # root = Tk()
    # root.title("___Ora Bolas___")
    # root.geometry(f"{high}x{large}")
    # root.maxsize(f"{high}",f"{large}")
    # root.minsize(f"{high}",f"{large}")
    # imgCampo = PhotoImage(file = path +"\\campo.png")
    # l_campo = Label(root,image = imgCampo)
    # l_campo.place(x=80,y=55)
    scale = 1.5
    w = int(900 * scale)
    h = int(600 * scale)

    root = Tk()
    root.title("Ora Bolas")
    root.geometry("{}x{}+0+0".format(w, h))
    root.maxsize(w, h)
    root.minsize(w, h)
    root.attributes('-topmost',True)

    C = Canvas(root, height=h, width=w)

    cont_interface = 0
    pixel_scale = int(100 * scale) #150
    vector_scale = float(1 / 5)    
 
    

    while(cont_interface != len(robo["x"])):
        C.delete("all")
        C.config(bg="#306324")
        C.pack()

        x0_robo_pixel = (robo["x"][cont_interface] * pixel_scale) - ((robo["raio"]) * scale)
        y0_robo_pixel = (robo["y"][cont_interface] * pixel_scale) - ((robo["raio"]) * scale)
        x_robo_pixel = (robo["x"][cont_interface] * pixel_scale) + ((robo["raio"]) * scale)
        y_robo_pixel = (robo["y"][cont_interface] * pixel_scale) + ((robo["raio"]) * scale)
        center_robo_pixel = [(robo["x"][cont_interface] * pixel_scale), (robo["y"][cont_interface] * pixel_scale)]
        v_robo_pixel = [((robo["x"][cont_interface] + (robo["v"][cont_interface][0] * vector_scale)) * pixel_scale), ((robo["y"][cont_interface] + (robo["v"][cont_interface][1] * vector_scale)) * pixel_scale)]
        a_robo_pixel = [((robo["x"][cont_interface] + (robo["a"][cont_interface][0]* vector_scale)) * pixel_scale), ((robo["y"][cont_interface] + (robo["a"][cont_interface][1] * vector_scale)) * pixel_scale)]
        v_mod_robo = math.sqrt((robo["v"][cont_interface][0] ** 2) + (robo["v"][cont_interface][1] ** 2))
        a_mod_robo = math.sqrt((robo["a"][cont_interface][0] ** 2) + (robo["a"][cont_interface][1] ** 2))

        x0_bola_pixel = (bola["x"][cont_interface] * pixel_scale) - ((bola["raio"]) * scale)
        y0_bola_pixel = (bola["y"][cont_interface] * pixel_scale) - ((bola["raio"]) * scale)
        x_bola_pixel = (bola["x"][cont_interface] * pixel_scale) + ((bola["raio"]) * scale)
        y_bola_pixel = (bola["y"][cont_interface] * pixel_scale) + ((bola["raio"]) * scale)
        center_bola_pixel = [(bola["x"][cont_interface] * pixel_scale), (bola["y"][cont_interface] * pixel_scale)]
        v_bola_pixel = [((bola["x"][cont_interface] + (bola["v"][cont_interface][0] * vector_scale)) * pixel_scale), ((bola["y"][cont_interface] + (bola["v"][cont_interface][1] * vector_scale)) * pixel_scale)]
        a_bola_pixel = [((bola["x"][cont_interface] + (bola["a"][cont_interface][0] * vector_scale)) * pixel_scale), ((bola["y"][cont_interface] + (bola["a"][cont_interface][1] * vector_scale)) * pixel_scale)]
        v_mod_bola = math.sqrt((bola["v"][cont_interface][0] ** 2) + (bola["v"][cont_interface][1] ** 2))
        a_mod_bola = math.sqrt((bola["a"][cont_interface][0] ** 2) + (bola["a"][cont_interface][1] ** 2))

        for i in range(0, cont_interface, 2):
            draw_robo_path = line = C.create_line((robo["x"][i] * pixel_scale), (h - (robo["y"][i] * pixel_scale)), (robo["x"][i + 1] * pixel_scale), (h - (robo["y"][i + 1] * pixel_scale)), fill="#333333", width=4)
            draw_bola_path = line = C.create_line((bola["x"][i] * pixel_scale), (h - (bola["y"][i] * pixel_scale)), (bola["x"][i + 1] * pixel_scale), (h - (bola["y"][i + 1] * pixel_scale)), fill="#bbbbbb", width=4)

            draw_robo_vel = C.create_line(center_robo_pixel[0], (h - center_robo_pixel[1]), v_robo_pixel[0], (h - v_robo_pixel[1]), arrow=LAST, width=3, fill="#95abc1")
            draw_bola_vel = C.create_line(center_bola_pixel[0], (h - center_bola_pixel[1]), v_bola_pixel[0], (h - v_bola_pixel[1]), arrow=LAST, width=3, fill="#fcdbe2")
            draw_robo_acc = C.create_line(center_robo_pixel[0], (h - center_robo_pixel[1]), a_robo_pixel[0], (h - a_robo_pixel[1]), arrow=LAST, width=3, fill="#e4d1e6")
            draw_bola_acc = C.create_line(center_bola_pixel[0], (h - center_bola_pixel[1]), a_bola_pixel[0], (h - a_bola_pixel[1]), arrow=LAST, width=3, fill="#f7b1bd")

            text_robo_vel = C.create_text(v_robo_pixel[0] + 25, (h - v_robo_pixel[1] + 25), text="|V| = {:.3g}".format(v_mod_robo), font=("Helvetica", "15", "bold"))
            text_bola_vel = C.create_text(v_bola_pixel[0] + 25, (h - v_bola_pixel[1] + 25), text="|V| = {:.3g}".format(v_mod_bola), font=("Helvetica", "15", "bold"))
            text_robo_acc = C.create_text(a_robo_pixel[0] + 25, (h - a_robo_pixel[1] + 25), text="|A| = {:.3g}".format(a_mod_robo), font=("Helvetica", "15", "bold"))
            text_bola_acc = C.create_text(a_bola_pixel[0] + 25, (h - a_bola_pixel[1] + 25), text="|A| = {:.3g}".format(a_mod_bola), font=("Helvetica", "15", "bold"))

            draw_robo = C.create_oval(x0_robo_pixel, (h - y0_robo_pixel), x_robo_pixel, (h - y_robo_pixel), fill="#000000")
            draw_bola = C.create_oval(x0_bola_pixel, (h - y0_bola_pixel), x_bola_pixel, (h - y_bola_pixel), fill="#ffffff")
            
        cont_interface += 1
        time.sleep(0.02)
        C.update()

    root.mainloop()

