# Nome: Bruno Arthur Basso Silva RA: 22.222.067-5
# Nome: Hugo Emilio Nomura RA: 22.123.051-9

# Professora: Simone

# Este arquivo contem todas as funções que serão utilizadas no programa principal

from matplotlib import pyplot as plt # para criar os gráficos
import math
import random
from time import sleep
import pandas as pd # manusear .xlsx 

# VARIAVEIS GLOBAIS
instante = 0
colisao = False
dist_euclidiana = []



# OBSERVAÇÃO: veja se o arquivo "trajetoria.xlsx" e o "funcoes.py" está na mesma pasta deste código

# Primeiro, criamos os elementos principais para a funcionalidade do programa
# utilizamos dicionarios para facilitar a visualização dos dados
bola = {
    "raio": 0.0215, 
    "t": [], # tempo
    "x": [], # posicao x
    "y": [], # posicao y
    "v": [], # velocidade
    "a": [], # aceleração
}

robo = {
    "raio": 0.09,
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
    print("Bruno Arthur Basso Silva")
    print("Hugo Emilio Nomura")
    print()
    sleep(1)
    get_robo_position()
    att_robo()
    createGraphics()

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
        robo_x = random.randrange(0, 901) / 100
        robo_y = random.randrange(0, 601) / 100
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
    dist_x = bola["x"][int(instante / 0.02)] - robo["x"][-1]
    dist_y = bola["y"][int(instante / 0.02)] - robo["y"][-1]

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
    # caso o robo não esteja em nenhum dos eixos, ele estará em um dos 4 quadrantes
    elif dist_x > 0 and dist_y > 0:
        Quad = 1
    elif dist_x < 0 and dist_y > 0:
        Quad = 2
    elif dist_x < 0 and dist_y < 0:
        Quad = 3
    elif dist_x > 0 and dist_y < 0:
        Quad = 4
    
    # Calculamos a tangente inversa
    if(dist_x != 0):
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
    # Pelos dados fornecidos, sabemos que a aceleracao maxima do robo é 2.8 m/s² e que o tempo é atualizado a cada 0.02s
    
    Vmax = 2.8 * 0.02
    ang = get_angulo()
    vetor_Vmax = [get_V0x(Vmax, ang), get_V0y(Vmax, ang)] # decomposicao vetorial da velocidade maxima

    # Caso o robo ainda não tenha atingido a velocidade maxima, ele acelera
    if(len(robo["a"]) > 0 and mod_Vetor(robo["v"]) < 2.8):
        acelerando = [vetor_Vmax[0] + robo["a"][-1][0], vetor_Vmax[1] + robo["a"][-1][1]] # acelerando o robo
        robo["a"].append(acelerando)
    else:
        robo["a"].append([0, 0]) # chegou na velocidade maxima e nao acelera mais

# getSpeedrobo(): pega a velocidade do robô.
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

    dist_x = bola["x"][int(instante / 0.02)] - robo["x"][-1]
    dist_y = bola["y"][int(instante / 0.02)] - robo["y"][-1]
    
    return math.sqrt(dist_x**2 + dist_y**2)

# Pegando o ponto de interceptação

def getInterceptionRadius():
    global collision
    global dist_euclidiana
    
    penetracao = bola["raio"] * 0.2

    dist = get_dist_euclidiana()
    intercept_radius = (robo["raio"] + bola["raio"] - penetracao) / 100

    if(dist > intercept_radius):
        dist_euclidiana.append(dist)

    else:
        dist_euclidiana.append(dist)
        collision = True
        
# Função que atualiza a aceleracao, velocidade e posição do robo a cada 0.02s caso não haja colisão
def att_robo():
    global instante
    
    get_dist_euclidiana()
    getInterceptionRadius()
    
    if(colisao == False):
        get_a_Robo()
        get_v_Robo()
        nextPositionRobo()
        instante += 0.02

# APROFUNDAMENTO! - Função que anima os vetores da bola e do robo na GUI
def Animando_vetores():
    temp_intercept = []

    for i in range(len(robo["x"])):
        temp_intercept.append(bola["t"][i])

    for i in range(len(temp_intercept)):
        time_gap = 0.02
        
        if bola["t"][i + 1] % 0.02 != 0:
            time_gap = bola["t"][i + 1] - bola["t"][i]

        bola["v"].append([(bola["x"][i + 1] - bola["x"][i]) / time_gap, (bola["y"][i + 1] - bola["y"][i]) / time_gap])
        bola["a"].append([(bola["v"][i][0] - bola["v"][i - 1][0]) / time_gap, (bola["v"][i][1] - bola["v"][i - 1][1]) / time_gap])


def createGraphics():
    robo_x2 = []
    robo_y2 = []
    robo_vx = []
    robo_vy = []
    robo_ax = []
    robo_ay = []

    bola_x2 = []
    bola_y2 = []
    bola_vx = []
    bola_vy = []
    bola_ax = []
    bola_ay = []

    time_interception = []

    for i in range(len(robo["x"])):
        bola_x2.append(bola["x"][i])
        bola_y2.append(bola["y"][i])
        robo_x2.append(robo["x"][i])
        robo_y2.append(robo["y"][i])
        time_interception.append(bola["t"][i])

    for i in range(len(time_interception)):
        time_gap = 0.02
        robo_vx.append(robo["v"][i][0])
        robo_vy.append(robo["v"][i][1])
        robo_ax.append(robo["a"][i][0])
        robo_ay.append(robo["a"][i][1])

        if bola["t"][i + 1] % 0.02 != 0:
            time_gap = bola["t"][i + 1] - bola["t"][i]

        bola_vx.append((bola["x"][i + 1] - bola["x"][i]) / time_gap)
        bola_vy.append((bola["y"][i + 1] - bola["y"][i]) / time_gap)
        bola_ax.append((bola_vx[i] - bola_vx[i - 1]) / time_gap)
        bola_ay.append((bola_vy[i] - bola_vy[i - 1]) / time_gap)

    
    while True:
        print("____________ABA DE GRAFICOS_____________")
        print()
        print("Qual gráfico você quer ver?")
        print("1 - ROBO")
        print("2 - BOLA")
        print("3 - BOLA / ROBO")
        print("0 - Sair")
        
        choice_obj = int(input())
        
        if(choice_obj == 1):
            print("Qual varivel você quer analisar do ROBO?")
            print("1 - X")
            print("2 - Vx")
            print("3 - ax")
            print("4 - Y")
            print("5 - Vy")
            print("6 - ay")
            
            choice_var = int(input())
            
            if(choice_var == 1):
                print(time_interception)
                print(robo_x2)
                plt.plot(time_interception, robo_x2)

                # Título e nome dos eixos
                plt.title("Gráfico das coordenadas X do robô em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("X")

                # Mostra o gráfico
                plt.show()
                
            elif(choice_var == 2):
                plt.plot(time_interception, robo_vx)

                # Título e nome dos eixos
                plt.title("Gráfico de velocidade em X do robô em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("VX")

                # Mostra o gráfico
                plt.show()
                return
            elif(choice_var == 3):
                plt.plot(time_interception, robo_ax)

                # Título e nome dos eixos
                plt.title("Gráfico da aceleração em X do robô em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("AX")

                # Mostra o gráfico
                plt.show()
                return
            elif(choice_var == 4):
                plt.plot(time_interception, robo_y2)

                # Título e nome dos eixos
                plt.title("Gráfico das coordenadas Y do robô em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("Y")

                # Mostra o gráfico
                plt.show()
                return
            elif(choice_var == 5):
                plt.plot(time_interception, robo_vy)

                # Título e nome dos eixos
                plt.title("Gráfico de velocidade em Y do robô em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("VY")

                # Mostra o gráfico
                plt.show()
                return
            elif(choice_var == 6):
                plt.plot(time_interception, robo_ay)

                # Título e nome dos eixos
                plt.title("Gráfico da aceleração em Y do robô em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("AY")

                # Mostra o gráfico
                plt.show()
                return
        
        elif(choice_obj == 2):
            print("Qual varivel você quer analisar da BOLA?")
            print("1 - X")
            print("2 - Vx")
            print("3 - ax")
            print("4 - Y")
            print("5 - Vy")
            print("6 - ay")
            choice_var = int(input())
            
            if(choice_var == 1):
                plt.plot(time_interception, bola_x2)

                # Título e nome dos eixos
                plt.title("Gráfico das coordenadas X da bola em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("X")

                # Mostra o gráfico
                plt.show()
                return
            elif(choice_var == 2):
                plt.plot(time_interception, bola_vx)

                # Título e nome dos eixos
                plt.title("Gráfico de velocidade em X da bola em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("VX")

                # Mostra o gráfico
                plt.show()
                return
            elif(choice_var == 3):
                plt.plot(time_interception, bola_ay)

                # Título e nome dos eixos
                plt.title("Gráfico da aceleração em Y da bola em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("AY")

                # Mostra o gráfico
                plt.show()
                return
            elif(choice_var == 4):
                plt.plot(time_interception, bola_y2)

                # Título e nome dos eixos
                plt.title("Gráfico das coordenadas Y da bola em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("Y")

                # Mostra o gráfico
                plt.show()
                return
            elif(choice_var == 5):
                plt.plot(time_interception, bola_vy)

                # Título e nome dos eixos
                plt.title("Gráfico de velocidade em Y da bola em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("VY")

                # Mostra o gráfico
                plt.show()
                return
            elif(choice_var == 6):
                plt.plot(time_interception, bola_ay)

                # Título e nome dos eixos
                plt.title("Gráfico da aceleração em Y da bola em função do tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("AY")

                # Mostra o gráfico
                plt.show()
                return
        elif(choice_obj == 3):
            plt.plot(robo_x2, robo_y2)
            plt.plot(bola_x2, bola_y2)
            plt.plot(bola["x"], bola["y"], 'r--')
            plt.plot(robo_x2[-1], robo_y2[-1], 'ro')
            plt.plot(bola_x2[-1], bola_y2[-1], 'ro')

            # Título e nome dos eixos
            plt.title("Gráfico da trajetória da bola e do robô.")
            plt.xlabel("X")
            plt.ylabel("Y")

            # Mostra o gráfico
            plt.show()
            return
        elif(choice_obj == 0):
            break
        else:
            print("Opção inválida.")
            return
        
