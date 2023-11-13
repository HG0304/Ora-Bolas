# Nome: Bruno Arthur Basso Silva RA: 22.222.067-5
# Nome: Hugo Emilio Nomura RA: 22.123.051-9

# Professora: Simone

# Este arquivo contem todas as funções que serão utilizadas no programa principal

import math
from ora_bolas import *
import random
from time import sleep

# VARIAVEIS GLOBAIS
instante = 0
colisao = False

# FUNCOES

def main():
    print("Seja muito bem vindo ao...")
    print()
    sleep(1)
    print(" ___________________ ")
    print("|                   |")
    print("|                   |")
    print("|    !ORA BOLAS!    |")
    print("|                   |")
    print("|___________________|")
    print()
    print("Integrantes!")
    print()
    print("Bruno Basso")
    print("Hugo Nomura")
    print()
    sleep(1)
    get_robo_position()

# get_V0x e get_V0y calculam as componentes x e y de um vetor a partir de um modulo e um angulo
def get_V0x(v0,ang):
    v0x = v0 * math.cos(math.radians(ang))  
    return v0x
    
def get_V0y(v0,ang):
    v0y = v0 * math.sin(math.radians(ang)) 
    return v0y

# primeiro, vamos iniciar o programa com uma função que irá carregar os dados do robo
def get_robo_position():
    print("Você gostaria de escolher a posição inicial ou criar uma posição aleatória?")
    print("1) Escolher posição inicial.")
    print("2) Criar posição inicial aletaória.")
    choice = int(input())

    if(choice == 1):
        print()
        print("Digite a posição do robô!")
        robo_x = float(input("Digite a posição X: "))
        robo_y = float(input("Digite a posição Y: "))
        robo["x"].append(robo_x)
        robo["y"].append(robo_y)

    elif(choice == 2):
        print()
        robo_x = random.randrange(0, 91) / 10
        robo_y = random.randrange(0, 61) / 10
        robo["x"].append(robo_x)
        robo["y"].append(robo_y)
        
    else:
        print("Opção inválida.\n")
        get_robo_position()
        
# Vamos testar se a posição inicial do robo é válida
def test_robo_position():
    if(robo["x"][0] < 0 or robo["x"][0] > 9):
        print("Posição inicial do robo inválida.\n")
        get_robo_position()
        test_robo_position()
        
    elif(robo["y"][0] < 0 or robo["y"][0] > 6):
        print("Posição inicial do robo inválida.\n")
        get_robo_position()
        test_robo_position()
        
    else:
        print("Posição inicial do robo válida.\n")
        
        
# Outra funcao importante é a que calcula o angulo entre o robo e a bola
def get_angulo():
    global instante
    Quad = 0 # Quadrante
    
    # Calculamos a distancia entre o robo e a bola em x e y
    dist_x = bola["x"][instante / 0.02] - robo["x"][-1]
    dist_y = bola["y"][instante / 0.02] - robo["y"][-1]

    # analisamos o quadrante em que o robo está e posteriormente calculamos a tangente inversa
    if dist_x == 0:
        if dist_y > 0:
            ang = math.pi / 2 # 90 graus
            return ang
        else:
            ang = 3 * (math.pi / 2) # 270 graus
            return ang
    if dist_y == 0:
        if dist_x > 0:
            ang = 0     # 0 graus
            return ang
        else:
            ang = math.pi # 180 graus
            return ang
    elif dist_x > 0 and dist_y > 0:
        Quad = 1
    elif dist_x < 0 and dist_y > 0:
        Quad = 2
    elif dist_x < 0 and dist_y < 0:
        Quad = 3
    elif dist_x > 0 and dist_y < 0:
        Quad = 4
    
    # Como citado anteriormente, calculamos a tangente inversa
    else:
        tg = 0
        if(Quad == 2 or Quad == 4): # Quadrantes espelhados geometricamente
            tg = abs(dist_x) / abs(dist_y)
        else:
            tg = abs(dist_y) / abs(dist_x)

        tg = math.atan(tg)
        ang = tg + (Quad - 1) * (math.pi / 2) # usado para ajustar o ângulo com base no quadrante em que ele se encontra
        return ang

# calcula o modulo de um vetor
def mod_Vetor(vetor):
    return math.sqrt(vetor[0][0]**2 + vetor[0][1]**2)

# Agora, vamos calcular a aceleracao do robo
def get_a_Robo():
    # Para calcularmos a aceleção do robo, precisamos calcular a velocidade maxima do robo
    # Para isso, vamos utilizar a formula da velocidade maxima
    # Vmax = Amax * t
    # Pelos dados fornecidos, sabemos que a aceleracao maxima do robo é 2.8 m/s²
    
    Vmax = 2.8 * 0.02
    ang = get_angulo()
    vetor_Vmax = [get_V0x(Vmax, ang), get_V0y(Vmax, ang)] # decomposicao vetorial da velocidade maxima

    if(len(robo["a"]) > 0 and mod_Vetor(robo["v"]) < 2.8):
        acelerando = [vetor_Vmax[0] + robo["a"][-1][0], vetor_Vmax[1] + robo["a"][-1][1]] # acelerando o robo
        robo["a"].append(acelerando)
    else:
        robo["a"].append([0, 0]) # chegou na velocidade maxima e nao acelera mais

# getSpeedRobot(): pega a velocidade do robô.
# e armazena em robo["v"]
def get_v_Robo():
    ang = get_angulo()

    if(robo["a"][-1] != [0, 0]):
        robo["v"].append([robo["v"][-1][0] + robo["a"][-1][0], robo["v"][-1][1] + robo["a"][-1][1]])
    else: 
        robo["v"].append([get_V0x(2.8, ang), get_V0y(2.8, ang)])

# pegando a proxima posicao do robo
def nextPositionRobo():
    robo["x"].append(robo["x"][-1] + robo["v"][-1][0])
    robo["y"].append(robo["y"][-1] + robo["v"][-1][1])




# Para a resolução do problema proposto, utilizaremos uma função para calcular a distancia euclidiana entre a bola e o robo
# A distancia euclidiana é a distancia entre dois pontos em um plano cartesiano
# A formula para calcular a distancia euclidiana é:
# d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
def get_dist_euclidiana():
    global instante

    dist_x = bola["x"][instante / 0.02] - robo["x"][-1]
    dist_y = bola["y"][instante / 0.02] - robo["y"][-1]
    
    return math.sqrt(dist_x**2 + dist_y**2)

# Pegando o ponto de interceptação

def getInterceptionPoint():
    global instante
    global colisao
    
    