# projetil balistico final.py
# LABORATORIO - MOV. BALISTICO
# Nome: Bruno Arthur Basso Silva RA: 22.222.067-5
# Nome: Hugo Emilio Nomura RA: 22.123.051-9

# Professora: Simone

import math

# VARIAVEIS GLOBAIS

# aceleracao da gravidade 
g = -9.8 # m/s^2

# v0 = 34.9
# ang = 42.9 # graus
# alty = 0.46 # altura do solo em metros
# td = 1.11 # tempo definido
    



# FUNCOES

def get_V0x(v0,ang):
    v0x = v0 * math.cos(math.radians(ang))  # transforma o angulo em radianos
    return v0x
    

def get_V0y(v0,ang):
    v0y = v0 * math.sin(math.radians(ang))  # transforma o angulo em radianos
    return v0y


def get_tempo_no_ar(v0, alty, ang):
    v0y = get_V0y(v0, ang)

    # Calcula o tempo de subida até o ponto mais alto
    t_subida = -v0y / g
    print(f"Tempo de subida: {t_subida:.2f}")

    # Calcula a altura máxima atingida
    h_max = (v0y**2 / (2 * g)) + alty

    # Calcula o tempo de descida do ponto mais alto até o chão
    t_descida = (math.sqrt(v0y**2 - 2 * g * (h_max - alty)) + abs(v0y)) / abs(g)
    print(f"Tempo de descida: {t_descida:.2f}")

    # O tempo total no ar é a soma do tempo de subida e descida
    t_total = t_subida + t_descida
    return t_total


def get_posicao_em_t(v0, alty, t, ang):
    v0y = get_V0y(v0, ang)
    v0x = get_V0x(v0, ang)

    # Calcula a posicao em t
    x = v0x * t
    y = (v0y * t) + (g * t**2 / 2) + alty
    return x, y
    
def get_vx_em_t(v0x, t):
    vx = v0x
    return vx

def get_vy_em_t(v0y, t):
    vy = v0y + g * t
    return vy

def get_v_em_t(v0x, v0y, t):
    vx = get_vx_em_t(v0x, t)
    vy = get_vy_em_t(v0y, t)
    v = math.sqrt(vx**2 + vy**2)
    return v

def h_max(v0, alty, ang):
    v0y = get_V0y(v0, ang)
    h_max = -(v0y**2 / (2*g)) + alty
    return h_max

def max_alcance(v0, alty, ang):
    v0x = get_V0x(v0, ang)
    t = get_tempo_no_ar(v0, alty)
    x = v0x * t
    return x + 0.1

# Calcule a velocidade da bola imediatamente antes de alcançar o solo e suas componentes nos eixos x e y
def get_v_antes_do_solo(v0, alty, ang):
    v0y = get_V0y(v0, ang)
    v0x = get_V0x(v0, ang)

    t = get_tempo_no_ar(v0, alty)

    vx = get_vx_em_t(v0x, t)
    vy = get_vy_em_t(v0y, t)
    v = get_v_em_t(v0x, v0y, t)
    return v, vx, vy

# Calcule a velocidade no instante em que a bola atinge a altura máxima e suas componentes nos eixos x e y.
def get_v_altura_max(v0, alty, ang):
    v0y = get_V0y(v0, ang)
    v0x = get_V0x(v0, ang)

    t = get_tempo_no_ar(v0, alty)
    
    vx = get_vx_em_t(v0x, t)
    vy = get_vy_em_t(v0y, t)
    v = get_v_em_t(v0x, v0y, t)
    return v, vx, vy
    

def get_velocidade_final(v0, alty, ang):
    y = h_max(v0, alty)
    vy = 2 * -g *y
    vfy = math.sqrt(vy)
    vfx = get_V0x(v0, 360 - ang)

    return vfx,-vfy