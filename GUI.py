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
    root.title("Ora Bolas - 3° semestre")
    root.geometry(f"{w}x{h}+0+0")
    root.maxsize(w, h)
    root.minsize(w, h)
    root.attributes('-topmost', True)
    janela = Canvas(root, height=h, width=w)
    
    
    janela.pack()


    contador = 0
    while(contador != len(robo["x"])):
        janela.delete("all")
        janela.config(bg="green")
        # Desenha as linhas laterais
        janela.create_line(10, 10, 10, h-80, width=3)  # Linha esquerda
        janela.create_line(w-10, 10, w-10, h-80, width=3)  # Linha direita

        # Desenha as linhas de fundo
        janela.create_line(10, 10, w-10, 10, width=3)  # Linha superior
        janela.create_line(10, h-80, w-10 , h-80, width=3)  # Linha inferior

        # Desenha a linha do meio-campo
        janela.create_line(w//2, 10, w/2, h-80, width=3)

        # Desenha os gols
        janela.create_rectangle(10, 550, 110, 280, fill="grey", outline="black", width=3)  # Área esquerda
        janela.create_rectangle(w-110, 550, w-10, 280,fill="grey", outline="black", width=3)  # Área direita
        
        # Desenha a área
        # Desenha os gols
        janela.create_rectangle(10, 720, 280, 150, outline="black", width=1.5)  # Área esquerda
        janela.create_rectangle(w-280, 720, w-10, 150, outline="black", width=1.5)  # Área direita

        # Adiciona o círculo no meio-campo
        janela.create_oval(w//2-130, h//2-130, w//2+130, h//2+130, outline="black", width=3)
        
        janela.create_oval(w//2 - 40, h//2 - 40, w//2 + 40, h//2 + 40, outline="black", width=3)

        
        x0_robo_pixel = (robo["x"][contador] * pixel_scale) - ((robo["raio"]) * 150)
        y0_robo_pixel = (robo["y"][contador] * pixel_scale) - ((robo["raio"]) * 150)
        x_robo_pixel = (robo["x"][contador] * pixel_scale) + ((robo["raio"]) * 150)
        y_robo_pixel = (robo["y"][contador] * pixel_scale) + ((robo["raio"]) * 150)

        x0_bola_pixel = (bola["x"][contador] * pixel_scale) - ((bola["raio"]) * 330)
        y0_bola_pixel = (bola["y"][contador] * pixel_scale) - ((bola["raio"])  * 330)
        x_bola_pixel = (bola["x"][contador] * pixel_scale) + ((bola["raio"])  * 330)
        y_bola_pixel = (bola["y"][contador] * pixel_scale) + ((bola["raio"])  * 330)

        for i in range(0, contador, 2):
            
            linha_robo  = janela.create_line((robo["x"][i] * pixel_scale), (h - (robo["y"][i] * pixel_scale)), (robo["x"][i + 1] * pixel_scale), (h - (robo["y"][i + 1] * pixel_scale)), fill="black", width=5)
            linha_bola  = janela.create_line((bola["x"][i] * pixel_scale), (h - (bola["y"][i] * pixel_scale)), (bola["x"][i + 1] * pixel_scale), (h - (bola["y"][i + 1] * pixel_scale)), fill="white", width=5)
            
            draw_robo = janela.create_oval(x0_robo_pixel, (h - y0_robo_pixel), x_robo_pixel, (h - y_robo_pixel), outline="black",fill="black", width=2)
            draw_bola = janela.create_oval(x0_bola_pixel, (h - y0_bola_pixel), x_bola_pixel, (h - y_bola_pixel), fill="white")
            
        time.sleep(0.02)
        contador += 1
        janela.update()
        

       

    root.mainloop()


