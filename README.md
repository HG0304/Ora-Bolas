# Ora-Bolas

## Descrição do Projeto

Ora-Bolas é um projeto desenvolvido para simular a interceptação de uma bola por um robô em um campo de futebol de robôs. O objetivo principal é calcular a trajetória do robô, considerando suas limitações físicas, para interceptar a bola em movimento. O projeto utiliza conceitos de física clássica, como aceleração, velocidade e ângulos, além de ferramentas de visualização gráfica e interface gráfica para exibir os resultados.

## Objetivos

- Simular a trajetória de um robô para interceptar uma bola em movimento.
- Implementar cálculos de cinemática para determinar a posição, velocidade e aceleração do robô e da bola.
- Criar gráficos para análise visual das variáveis físicas envolvidas.
- Desenvolver uma interface gráfica para visualização em tempo real da simulação.
- Garantir a precisão dos cálculos e a usabilidade do sistema.

## Principais Características

- **Cálculos de Cinemática:** Implementação de funções para calcular ângulos, velocidades e acelerações do robô e da bola.
- **Visualização Gráfica:** Geração de gráficos utilizando a biblioteca `matplotlib` para análise das variáveis físicas.
- **Interface Gráfica:** Uso de `tkinter` para criar uma interface que simula o campo de futebol e exibe a trajetória do robô e da bola em tempo real.
- **Animação:** Representação animada dos vetores de velocidade e aceleração do robô e da bola.
- **Leitura de Dados:** Integração com arquivos Excel para carregar os dados de trajetória da bola.

## Desafios Superados

- **Cálculo Preciso de Trajetórias:** Implementação de algoritmos para calcular a trajetória do robô com base em sua posição inicial e nas limitações de velocidade e aceleração.
- **Sincronização de Dados:** Garantir que os cálculos de posição, velocidade e aceleração estejam sincronizados com os dados de tempo.
- **Visualização em Tempo Real:** Desenvolvimento de uma interface gráfica que atualiza a posição do robô e da bola em tempo real, mantendo a fluidez da animação.
- **Tratamento de Erros:** Implementação de validações para garantir que as posições iniciais do robô sejam válidas e dentro dos limites do campo.
- **Integração de Múltiplas Bibliotecas:** Uso de bibliotecas como `matplotlib`, `tkinter` e `pandas` de forma integrada para atender aos requisitos do projeto.

## Tecnologias Utilizadas

- **Python:** Linguagem principal do projeto.
- **Matplotlib:** Para criação de gráficos.
- **Tkinter:** Para desenvolvimento da interface gráfica.
- **Pandas:** Para manipulação de dados em arquivos Excel.
- **PyInstaller:** Para criação de um executável do projeto.

## Modo de Uso

1. **Instale as dependências:** Certifique-se de que as bibliotecas `matplotlib`, `openpyxl` e `pandas` estão instaladas. Você pode instalá-las com o comando:
   ```bash
   pip install matplotlib
   ```
   ```bash
   pip install openpyxl
   ```
   ```bash
   pip install pandas
   ```
2. **Execute o arquivo ora_bolas.py**:
    ```bash
   python ora_bolas.py
   ```

## Possíveis Melhorias

- Adicionar suporte para múltiplos robôs no campo.
- Implementar inteligência artificial para prever a trajetória da bola e otimizar a interceptação.
- Melhorar a interface gráfica com elementos mais modernos e responsivos.
- Adicionar testes automatizados para validar os cálculos e a lógica do programa.

## Conclusão

Este projeto demonstra habilidades em programação, física aplicada, visualização de dados e desenvolvimento de interfaces gráficas. Ele é um exemplo prático de como resolver problemas complexos utilizando conceitos de cinemática e ferramentas de software. Além disso, destaca a capacidade de superar desafios técnicos e entregar uma solução funcional e visualmente atraente.