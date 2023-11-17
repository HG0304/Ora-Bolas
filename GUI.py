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
    WIDTH = int(900 * scale)
    h = int(600 * scale)
    escala_gui = int(100 * scale)

    root = Tk()
    root.title("Ora Bolas - 2° semestre")
    root.geometry(f"{WIDTH}x{h}+0+0")
    root.maxsize(WIDTH, h)
    root.minsize(WIDTH, h)
    root.attributes('-topmost', True)
    janela = Canvas(root, height=h, width=WIDTH)
    
    
    janela.pack()


    contador = 0
    while(contador != len(robo["x"])):
        janela.delete("all")
        janela.config(bg="green")
        # Desenha as linhas laterais
        janela.create_line(10, 10, 10, h-80, width=3)  # Linha esquerda
        janela.create_line(WIDTH-10, 10, WIDTH-10, h-80, width=3)  # Linha direita

        # Desenha as linhas de fundo
        janela.create_line(10, 10, WIDTH-10, 10, width=3)  # Linha superior
        janela.create_line(10, h-80, WIDTH-10 , h-80, width=3)  # Linha inferior

        # Desenha a linha do meio-campo
        janela.create_line(WIDTH//2, 10, WIDTH/2, h-80, width=3)

        # Desenha os gols
        janela.create_rectangle(10, 550, 110, 280, fill="grey", outline="black", width=3)  # Área esquerda
        janela.create_rectangle(WIDTH-110, 550, WIDTH-10, 280,fill="grey", outline="black", width=3)  # Área direita
        
        # Desenha os gols
        janela.create_rectangle(10, 720, 280, 150, outline="black", width=1.5)  # Área esquerda
        janela.create_rectangle(WIDTH-280, 720, WIDTH-10, 150, outline="black", width=1.5)  # Área direita

        # Adiciona o círculo no meio-campo
        janela.create_oval(WIDTH//2-130, h//2-130, WIDTH//2+130, h//2+130, outline="black", width=3)
        
        janela.create_oval(WIDTH//2 - 10, h//2 - 10, WIDTH//2 + 10, h//2 + 10,fill="black", outline="black", width=3)

        # calculando cada pixel do robo
        
        x0_robo_pixel = (robo["x"][contador] * escala_gui) - ((robo["raio"]) * 150)
        y0_robo_pixel = (robo["y"][contador] * escala_gui) - ((robo["raio"]) * 150)
        x_robo_pixel = (robo["x"][contador] * escala_gui) + ((robo["raio"]) * 150)
        y_robo_pixel = (robo["y"][contador] * escala_gui) + ((robo["raio"]) * 150)

        centralizar_vetor_robo = [(robo["x"][contador] * escala_gui), (robo["y"][contador] * escala_gui)]

        # calculando cada pixel da bola
        
        x0_bola_pixel = (bola["x"][contador] * escala_gui) - ((bola["raio"]) * 330)
        y0_bola_pixel = (bola["y"][contador] * escala_gui) - ((bola["raio"])  * 330)
        x_bola_pixel = (bola["x"][contador] * escala_gui) + ((bola["raio"])  * 330)
        y_bola_pixel = (bola["y"][contador] * escala_gui) + ((bola["raio"])  * 330)
        
        centralizar_vetor_bola = [(bola["x"][contador] * escala_gui), (bola["y"][contador] * escala_gui)]
        
        # fazendo o vetor velocidade e aceleracao do robo
        v_robo = [((robo["x"][contador] + (robo["v"][contador][0] * 0.2)) * escala_gui), ((robo["x"][contador] + (robo["v"][contador][1] * 0.2)) * escala_gui)]
        a_robo = [((robo["x"][contador] + (robo["a"][contador][0] * 0.2)) * escala_gui), ((robo["x"][contador] + (robo["a"][contador][1] * 0.2)) * escala_gui)]

        # fazendo o vetor velocidade e aceleracao do robo
        v_bola = [((bola["x"][contador] + (bola["v"][contador][0] * 0.2)) * escala_gui), ((bola["x"][contador] + (bola["v"][contador][1] * 0.2)) * escala_gui)]
        a_bola = [((bola["x"][contador] + (bola["a"][contador][0] * 0.2)) * escala_gui), ((bola["x"][contador] + (bola["a"][contador][1] * 0.2)) * escala_gui)]
        
        
        for i in range(0, contador, 2):
            # desenhando as linhas de trajetoria tanto do robo quanto da bola
            janela.create_line((robo["x"][i] * escala_gui), (h - (robo["y"][i] * escala_gui)), (robo["x"][i + 1] * escala_gui), (h - (robo["y"][i + 1] * escala_gui)), fill="black", width=5)
            janela.create_line((bola["x"][i] * escala_gui), (h - (bola["y"][i] * escala_gui)), (bola["x"][i + 1] * escala_gui), (h - (bola["y"][i + 1] * escala_gui)), fill="white", width=5)
            
            # desenhando o robo e a bola
            janela.create_oval(x0_robo_pixel, (h - y0_robo_pixel), x_robo_pixel, (h - y_robo_pixel), outline="black",fill="black", width=2)
            janela.create_oval(x0_bola_pixel, (h - y0_bola_pixel), x_bola_pixel, (h - y_bola_pixel), fill="white")
            
            # desenhando os vetores do robo e da bola
            
            janela.create_line(centralizar_vetor_robo[0], h - centralizar_vetor_robo[1], v_robo[0], h - v_robo[1], arrow="last", width=2)
            janela.create_line(centralizar_vetor_robo[0], h - centralizar_vetor_robo[1], a_robo[0], h - a_robo[1], arrow="last", width=2)
            janela.create_line(centralizar_vetor_bola[0], h - centralizar_vetor_bola[1], v_bola[0], h - v_bola[1], arrow="last", width=2)
            janela.create_line(centralizar_vetor_bola[0], h - centralizar_vetor_bola[1], a_bola[0], h - a_bola[1], arrow="last", width=2)
            
            # desenhando o texto do vetor velocidade e aceleracao do robo
            janela.create_text(v_robo[0] + 40, h-v_robo[1] + 40, text="|→v| do robo:", font=(("Helvetica", "15", "bold")))
            janela.create_text(a_robo[0] + 40, h-a_robo[1] + 40, text="|→a| do robo:", font=("Helvetica", "15", "bold") )
            
            # desenhando o texto do vetor velocidade da bola
            janela.create_text(v_bola[0] + 40, h-v_bola[1] + 40,  text="|→v| da bola:", font=("Helvetica", "15", "bold"))
            janela.create_text(a_bola[0] + 40, h-a_bola[1] + 40,  text="|→a| da bola:", font=("Helvetica", "15", "bold"))
            
            
        time.sleep(0.02)
        contador += 1
        janela.update()

       

    root.mainloop()


