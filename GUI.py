# tkinter para fazer a interface gráfica
from tkinter import *
import math
import time
from time import sleep

# usamos essa importação para pegar a imagem de
# qualquer pasta em que ela estiver, basta fazer esse
# simples path e conseguimos manusear a imagem com facilidade
import os
scale = 1.5
WIDTH = int(900 * scale)
HEIGHT = int(600 * scale)
escala_gui = int(100 * scale)


def instanciarJanela(robo, bola):
    global scale, WIDTH, HEIGHT, escala_gui, root, janela
    root = Tk()

    root.title("Ora Bolas - 2° semestre")
    root.geometry(f"{WIDTH}x{HEIGHT}+0+0")
    root.maxsize(WIDTH + 10, HEIGHT + 10)
    root.minsize(WIDTH + 10, HEIGHT + 10)
    root.attributes('-topmost', True)
    janela = Canvas(root, height=HEIGHT, width=WIDTH)
    # Adiciona a legenda ao canto superior
    legenda_robo = Label(root, text="Robô", font=("Times New Roman", "12", "bold"), fg="black")
    legenda_robo.place(x=15, y=12)

    legenda_bola = Label(root, text="Bola ", font=("Times New Roman", "12", "bold"), fg="red")
    legenda_bola.place(x= 15, y=37)
    
    janela.pack()
    GUI_campo(robo,bola,janela,root)
    


def reiniciarJanela(contador,robo,bola,janela,root):
    contador = 0
    GUI_campo(robo,bola,janela,root)
    
    
def configurarBotaoReiniciar(w, h,contador,robo,bola,janela,root):
    botao_reiniciar = Button(root, text="Reiniciar animação!", command=lambda: reiniciarJanela(contador,robo,bola,janela,root))
    botao_reiniciar.place(x=w / 2 - 100, y=12, width=200, height=50)
    botao_reiniciar.config(bg="grey")
    botao_reiniciar.lift()
    

def GUI_campo(robo, bola,janela,root):
    
    contador = 0
    while(contador != len(robo["x"])):
        janela.delete("all")
        janela.config(bg="green")
        

        # Desenha as linhas laterais
        janela.create_line(10, 10, 10, HEIGHT-80, width=3)  # Linha esquerda
        janela.create_line(WIDTH-10, 10, WIDTH-10, HEIGHT-80, width=3)  # Linha direita

        # Desenha as linhas de fundo
        janela.create_line(10, 10, WIDTH-10, 10, width=3)  # Linha superior
        janela.create_line(10, HEIGHT-80, WIDTH-10 , HEIGHT-80, width=3)  # Linha inferior

        # Desenha a linha do meio-campo
        janela.create_line(WIDTH//2, 10, WIDTH/2, HEIGHT-80, width=3)

        # Desenha os gols
        janela.create_rectangle(10, 550, 110, 280, fill="green", outline="black", width=3)  # Área esquerda
        janela.create_rectangle(WIDTH-110, 550, WIDTH-10, 280,fill="green", outline="black", width=3)  # Área direita
        
        # Desenha os gols
        janela.create_rectangle(10, 720, 280, 110, outline="black", width=1.5)  # Área esquerda
        janela.create_rectangle(WIDTH-280, 720, WIDTH-10, 110, outline="black", width=1.5)  # Área direita
        
        # Adiciona o círculo no meio-campo
        janela.create_oval(WIDTH//2-130, HEIGHT//2-130, WIDTH//2+130, HEIGHT//2+130, outline="black", width=3)
        
        janela.create_oval(WIDTH//2 - 10, HEIGHT//2 - 10, WIDTH//2 + 10, HEIGHT//2 + 10,fill="black", outline="black", width=3)

        # calculando cada pixel do robo
        
        x0_robo_pixel = (robo["x"][contador] * escala_gui) - ((robo["raio"]) * 150)
        y0_robo_pixel = (robo["y"][contador] * escala_gui) - ((robo["raio"]) * 150)
        x_robo_pixel = (robo["x"][contador] * escala_gui) + ((robo["raio"]) * 150)
        y_robo_pixel = (robo["y"][contador] * escala_gui) + ((robo["raio"]) * 150)

        centralizar_vetor_robo = [(robo["x"][contador] * escala_gui), (robo["y"][contador] * escala_gui)]
        
        # fazendo o vetor velocidade e aceleracao do robo
        v_robo = [((robo["x"][contador] + (robo["v"][contador][0] * 0.2)) * escala_gui), ((robo["y"][contador] + (robo["v"][contador][1] * 0.2)) * escala_gui)]
        a_robo = [((robo["x"][contador] + (robo["a"][contador][0] * 0.2)) * escala_gui), ((robo["y"][contador] + (robo["a"][contador][1] * 0.2)) * escala_gui)]

        # calculando cada pixel da bola
        
        x0_bola_pixel = (bola["x"][contador] * escala_gui) - ((bola["raio"]) * 330)
        y0_bola_pixel = (bola["y"][contador] * escala_gui) - ((bola["raio"])  * 330)
        x_bola_pixel = (bola["x"][contador] * escala_gui) + ((bola["raio"])  * 330)
        y_bola_pixel = (bola["y"][contador] * escala_gui) + ((bola["raio"])  * 330)
        
        centralizar_vetor_bola = [(bola["x"][contador] * escala_gui), (bola["y"][contador] * escala_gui)]
        

        # fazendo o vetor velocidade e aceleracao do robo
        v_bola = [((bola["x"][contador] + (bola["v"][contador][0] * 0.2)) * escala_gui), ((bola["y"][contador] + (bola["v"][contador][1] * 0.2)) * escala_gui)]
        a_bola = [((bola["x"][contador] + (bola["a"][contador][0] * 0.2)) * escala_gui), ((bola["y"][contador] + (bola["a"][contador][1] * 0.2)) * escala_gui)]
        
        
        v_v_robo = math.sqrt((robo["v"][contador][0] ** 2) + (robo["v"][contador][1] ** 2))
        v_a_robo = math.sqrt((robo["a"][contador][0] ** 2) + (robo["a"][contador][1] ** 2))
        
        v_v_bola = math.sqrt((bola["v"][contador][0] ** 2) + (bola["v"][contador][1] ** 2))
        v_a_bola = math.sqrt((bola["a"][contador][0] ** 2) + (bola["a"][contador][1] ** 2))
        legenda_vetor_v_robo = Label(root, text=f"Velocidade: {v_v_robo:.2f} ", font=("Times New Roman", "12", "bold"), fg="black")
        legenda_vetor_a_robo = Label(root, text=f"Aceleração: {v_a_robo:.2f} ", font=("Times New Roman", "12", "bold"), fg="black")
        legenda_vetor_v_bola = Label(root, text=f"Velocidade: {v_v_bola:.2f} ", font=("Times New Roman", "12", "bold"), fg="red")
        legenda_vetor_a_bola = Label(root, text=f"Aceleração: {v_a_bola:.2f} ", font=("Times New Roman", "12", "bold"), fg="red")
        legenda_vetor = Label(root,text="VETORES!", font=("Times New Roman", "20","bold"), fg="grey")
        for i in range(0, contador, 2):
            # desenhando as linhas de trajetoria tanto do robo quanto da bola
            janela.create_line((robo["x"][i] * escala_gui), (HEIGHT - (robo["y"][i] * escala_gui)), (robo["x"][i + 1] * escala_gui), (HEIGHT - (robo["y"][i + 1] * escala_gui)), fill="black", width=5)
            janela.create_line((bola["x"][i] * escala_gui), (HEIGHT - (bola["y"][i] * escala_gui)), (bola["x"][i + 1] * escala_gui), (HEIGHT - (bola["y"][i + 1] * escala_gui)), fill="red", width=5)
            
            # desenhando o robo e a bola
            janela.create_oval(x0_robo_pixel, (HEIGHT - y0_robo_pixel), x_robo_pixel, (HEIGHT - y_robo_pixel), outline="black",fill="black", width=2)
            janela.create_oval(x0_bola_pixel, (HEIGHT - y0_bola_pixel), x_bola_pixel, (HEIGHT - y_bola_pixel), fill="red")
            
            # desenhando os vetores do robo e da bola
            
            janela.create_line(centralizar_vetor_robo[0], HEIGHT - centralizar_vetor_robo[1], v_robo[0], HEIGHT - v_robo[1], arrow="last", width=2)
            janela.create_line(centralizar_vetor_robo[0], HEIGHT - centralizar_vetor_robo[1], a_robo[0], HEIGHT - a_robo[1], arrow="last", width=2)
            janela.create_line(centralizar_vetor_bola[0], HEIGHT - centralizar_vetor_bola[1], v_bola[0], HEIGHT - v_bola[1], arrow="last", width=2, fill="red")
            janela.create_line(centralizar_vetor_bola[0], HEIGHT - centralizar_vetor_bola[1], a_bola[0], HEIGHT - a_bola[1], arrow="last", width=2, fill="red")
            
            # desenhando o texto do vetor velocidade e aceleracao do robo
            janela.create_text(v_robo[0] + 25, HEIGHT-v_robo[1] + 25, text="|→v|", font=(("Times New Roman", "15", "bold")))
            janela.create_text(a_robo[0] + 25, HEIGHT-a_robo[1] + 25, text="|→a|", font=("Times New Roman", "15", "bold") )
            
            # desenhando o texto do vetor velocidade da bola
            janela.create_text(v_bola[0] + 25, HEIGHT-v_bola[1] + 25,  text="|→v|", font=("Times New Roman", "15", "bold"))
            janela.create_text(a_bola[0] + 25, HEIGHT-a_bola[1] + 25,  text="|→a|", font=("Times New Roman", "15", "bold"))
            
            legenda_vetor.place(x = WIDTH - 170, y = 13)
            legenda_vetor_v_robo.place(x = WIDTH - 170, y = 53)
            legenda_vetor_a_robo.place(x = WIDTH - 170, y = 73)
            legenda_vetor_v_bola.place(x = WIDTH - 170, y = 93)
            legenda_vetor_a_bola.place(x = WIDTH - 170, y = 113)
        time.sleep(0.02)
        contador += 1
        janela.update()
        
        
    if contador == len(robo["x"]):   
        configurarBotaoReiniciar(WIDTH,HEIGHT, contador, robo, bola,janela, root)
        janela.update()
        
    
    root.mainloop()