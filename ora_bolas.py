# PROJETO ORA BOLAS
# Nome: Bruno Arthur Basso Silva RA: 22.222.067-5
# Nome: Hugo Emilio Nomura RA: 22.123.051-9

# Professora: Simone


#_______________________________________________________________________________
# Descrição do projeto:

# Objetivo: fazer um robô que intercepte a bola a partir de uma posição inicial definida pelo usuário
# Algorítmo escolhido para realização do trabalho: robô caçador

# Robô escolhido: small-size
# aceleracao - 2.8 m/s²
# velocidade - 2.8 m/s
# raio - 9 cm

# Bola:
# raio - 2.15 cm

# O arquivo chamado trajetoria.xlsx contem a posição
# da bola (coordenadas 𝑥 e 𝑦) a cada 0.02s

# O campo de futebol de robôs é um retângulo de
# 9,0 m × 6,0 m, que cada área é um retângulo de 0,5 m × 1,0 m e que as marcas
# de pênalti ficam a 2,0 m das linhas de fundo


# ------ IMPORTANTE ------
# CRIAR UM ARQUIVO EXECUTAVEL (VULGO EXE)
# DEFINIR Vmax E Amax (justificar a resposta)

import matplotlib.pyplot as plt
import pandas as pd
import math
from funcoes import *


# Primeiro, criamos os elementos principais para a funcionalidade do programa
# utilizamos dicionarios para facilitar a visualização dos dados
bola = {
    "raio": 0.0215,
    "t": [],
    "x": [],
    "y": [],
    "v": [],
    "a": [],
}

robo = {
    "raio": 0.09,
    "x": [],
    "y": [],
    "v": [[0, 0]],
    "a": [[0, 0]],
}

# Agora, precisamos extrair os dados da bola do arquivo .xlsx
# Carregar o arquivo .xlsx em um DataFrame do pandas
df = pd.read_excel('trajetoria.xlsx')

# Inserimos os dados da bola no dicionario bola
bola["t"] = df['t (s)'].tolist()
bola["x"] = df['x (m)'].tolist()
bola["y"] = df['y (m)'].tolist()

