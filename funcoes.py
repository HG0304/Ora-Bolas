# Nome: Bruno Arthur Basso Silva RA: 22.222.067-5
# Nome: Hugo Emilio Nomura RA: 22.123.051-9

# Professora: Simone

# Este arquivo contem todas as funções que serão utilizadas no programa principal

from matplotlib import pyplot as plt # para criar os gráficos
import math
import random
from time import sleep
import pandas as pd # manusear .xlsx 
from grafico import createGraphics # puxando os graficos do outro codigo
from GUI import *

# VARIAVEIS GLOBAIS
# Estas variaveis serão utilizadas em mais de uma função e por isso foram declaradas como globais
instante = 0
colisao = False
dist_euclidiana = []

# OBSERVAÇÃO: veja se o arquivo "trajetoria.xlsx" e o "funcoes.py" está na mesma pasta deste código

# Primeiro, criamos os elementos principais para a funcionalidade do programa
# utilizamos dicionarios para facilitar a visualização dos dados
bola = {
    "raio": 0.0215, # raio da bola em metros
    "t": [], # tempo
    "x": [], # posicao x
    "y": [], # posicao y
    "v": [], # velocidade
    "a": [], # aceleração
}

robo = {
    "raio": 0.09, # raio do robo em metros
    "x": [], # posicao x
    "y": [], # posicao y
    "v": [[0, 0]], # velocidade
    "a": [[0, 0]], # aceleração
}

# Agora, precisamos extrair os dados da bola do arquivo .xlsx
# Carregar o arquivo .xlsx em um DataFrame do pandas
df = pd.read_excel('trajetoria.xlsx')

# Inserimos os dados da bola no dicionario bola
bola["t"] = df['t (s)'].tolist()
bola["x"] = df['x (m)'].tolist()
bola["y"] = df['y (m)'].tolist()



# FUNCOES


def main():
    print("Seja muito bem vindo ao...")
    sleep(0.5)
    print(" ___________________ ")
    print("|                   |")
    print("|                   |")
    print("|     ORA BOLAS     |")
    print("|                   |")
    print("|___________________|")
    print()
    print("Integrantes!")
    print("- Bruno Arthur Basso Silva")
    print("- Hugo Emilio Nomura")
    
    get_robo_pos()
    test_robo_position()
    sleep(1)
    print("Calculando...")
    sleep(1)
    print("Veja a distância do robô se aproximando da bola...")
    sleep(1.8)
    print()
    
    while not colisao:
        att_robo()
    else:
        Animando_vetores(robo,bola)
        GUI_campo(robo,bola)
        createGraphics(robo,bola)

# get_V0x e get_V0y calculam as componentes x e y de um vetor a partir de um modulo e um angulo
def get_V0x(v0,ang): 
    return v0 * math.cos(ang)
    
def get_V0y(v0,ang):
    return v0 * math.sin(ang) 

# primeiro, vamos iniciar o programa com uma função que irá carregar os dados do robo
def get_robo_pos():
    print('\nDigite a opção desejada:')
    print()
    print("1 - Escolher posição inicial.")
    print("2 - Gerar posição inicial aleatória.")
    choice = int(input("--> "))

    if(choice == 1):
        print("\nDigite a posição do robô!")
        print()
        print("Posição X:")
        robo_x = float(input("--> "))
        print("Posição Y:")
        robo_y = float(input("--> "))
        robo["x"].append(robo_x)
        robo["y"].append(robo_y)

    elif(choice == 2):
        print()
        robo_x = random.randrange(0, 901) / 100
        robo_y = random.randrange(0, 601) / 100
        robo["x"].append(robo_x)
        robo["y"].append(robo_y)
        
    else:
        print("Opção inválida.\n")
        get_robo_pos()
        
# Vamos testar se a posição inicial do robo é válida
def test_robo_position():
    if(robo["x"][-1] < 0 or robo["x"][-1] > 9):
        print("Posição X do robo inválida.\n")
        get_robo_pos()
        test_robo_position()
        
    elif(robo["y"][-1] < 0 or robo["y"][-1] > 6):
        print("Posição Y do robo inválida.\n")
        get_robo_pos()
        test_robo_position()
        
        
     
        
        
# Outra funcao importante é a que calcula o angulo entre o robo e a bola
def calcular_distancia(instante):
    indice = int(instante / 0.02)
    dist_x = bola["x"][indice] - robo["x"][-1]
    dist_y = bola["y"][indice] - robo["y"][-1]
    return dist_x, dist_y

def get_angulo():
    global instante
    PI = math.pi
    PI_MEIO = PI / 2
    PI_DOIS = 2 * PI
    PI_TRES_MEIOS = 3 * PI_MEIO

    # Calculamos a distancia entre o robo e a bola em x e y
    dist_x, dist_y = calcular_distancia(instante)

    # analisamos o quadrante em que o robo está e posteriormente calculamos a tangente inversa
    if dist_x == 0:
        if dist_y > 0:
            return PI_MEIO # 90 graus
        else:
            return PI_TRES_MEIOS # 270 graus
    elif dist_y == 0:
        if dist_x > 0:
            return 0     # 0 graus
        else:
            return PI # 180 graus

    # caso o robo não esteja em nenhum dos eixos, ele estará em um dos 4 quadrantes
    if dist_x > 0 and dist_y > 0:
        quadrante = 1
    elif dist_x < 0 and dist_y > 0:
        quadrante = 2
    elif dist_x < 0 and dist_y < 0:
        quadrante = 3
    elif dist_x > 0 and dist_y < 0:
        quadrante = 4

    # Calculamos a tangente inversa
    if(dist_x != 0):
        tg = abs(dist_y / dist_x) if quadrante in [1, 3] else abs(dist_x / dist_y)
        
        # usado para ajustar o ângulo com base no quadrante em que ele se encontra
        angulo = math.atan(tg) + (quadrante - 1) * PI_MEIO 
        return angulo

# calcula o modulo de um vetor
def get_mod_vetor(vetor):
    return math.sqrt(vetor[-1][0]**2 + vetor[-1][1]**2)

def get_v_Robo():
    ang = get_angulo()
       
    if(robo["a"][-1] != [0, 0]):
        robo["v"].append([robo["v"][-1][0] + robo["a"][-1][0], robo["v"][-1][1] + robo["a"][-1][1]])
    else:
        robo["v"].append([get_V0x(2.8, ang), get_V0y(2.8, ang)])

# Agora, vamos definir a aceleracao do robo
def get_a_Robo(velocidade):
    # Para calcularmos a aceleção do robo, precisamos calcular a velocidade maxima do robo
    # Para isso, vamos utilizar a formula da velocidade maxima
    # Vmax = Amax * t
    # Pelos dados fornecidos, sabemos que a aceleracao maxima do robo é 2.8 m/s² e que o tempo é atualizado a cada 0.02s

    ang = get_angulo()
    
    vetor_V = [get_V0x(velocidade, ang), get_V0y(velocidade, ang)] # decomposicao vetorial da velocidade maxima

    # Caso o robo ainda não tenha atingido a velocidade maxima, ele acelera
    
    if(get_mod_vetor(robo["v"]) < 2.8):
        acelerando = [vetor_V[0] + robo["a"][-1][0], vetor_V[1] + robo["a"][-1][1]] # acelerando o robo
        robo["a"].append(acelerando)
    else:
        robo["a"].append([0, 0]) # chegou na velocidade maxima e nao acelera mais

# Agora, vamos definir a velocidade do robo


# Para a resolução do problema proposto, utilizaremos uma função para calcular a distancia euclidiana entre a bola e o robo
# A distancia euclidiana é a distancia entre dois pontos em um plano cartesiano
# A formula para calcular a distancia euclidiana é:
# d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
def get_dist_euclidiana():
    global instante

    dist_x, dist_y = calcular_distancia(instante)
    
    return math.sqrt(dist_x**2 + dist_y**2)

# Pegando o raio de interceptação
def get_r_interceptacao():
    global colisao
    global dist_euclidiana
    
    # Margem de erro de 20% do diametro da bola
    porcentagem = bola["raio"] * 2 * 0.2 # valor esperado de saida 0.0086 m

    dist = get_dist_euclidiana()
    intercept_radius = (robo["raio"] + bola["raio"] - porcentagem) # RI = 0.1029 m
    
    
    
    print(dist)

    if(dist > intercept_radius):
        dist_euclidiana.append(dist)
        
    elif(dist <= intercept_radius):
        dist_euclidiana.append(dist)
        colisao = True
        

# Função que atualiza a aceleracao, velocidade e posição do robo a cada 0.02s caso não haja colisão
def att_robo():
    sleep(0.02)
    global instante
    global colisao
    
    dist = get_dist_euclidiana()
    get_r_interceptacao()

    
    if(colisao == False):
        Vmax = 2.8 * 0.02
        
        get_a_Robo(Vmax)
        get_v_Robo()
        
        # atualiza posicao do robo
        robo["x"].append(robo["x"][-1] + robo["v"][-1][0] * 0.02)
        robo["y"].append(robo["y"][-1] + robo["v"][-1][1] * 0.02)
            
        instante += 0.02


# APROFUNDAMENTO! - Função que anima os vetores da bola e do robo na GUI
# uma vez que temos o tempo de interceptação atraves do tamanho da lista do robo["x"],
# podemos calcular a velocidade e a aceleração da bola para cada intevalo de tempo
# antes do ponto de interceptacao

def Animando_vetores(robo,bola):

    for i in range(len(robo["x"])):
        time_gap = 0.02
        
        bola["v"].append([(bola["x"][i + 1] - bola["x"][i]) / time_gap, (bola["y"][i + 1] - bola["y"][i]) / time_gap])
        bola["a"].append([(bola["v"][i][0] - bola["v"][i - 1][0]) / time_gap, (bola["v"][i][1] - bola["v"][i - 1][1]) / time_gap])