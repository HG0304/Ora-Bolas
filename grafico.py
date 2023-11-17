from matplotlib import pyplot as plt # para criar os gráficos

def createGraphics(robo,bola,dist_euclidiana):
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
        print("\n\n____________ABA DE GRAFICOS_____________")
        print()
        print("Qual gráfico você quer ver?")
        print("1 - ROBO")
        print("2 - BOLA")
        print("3 - BOLA / ROBO")
        print("4 - DISTANCIA ""D"" ENTRE O ROBO E A BOLA PELO TEMPO")
        print("0 - Sair") 
        
        choice_obj = int(input("-> "))
        
        if(choice_obj == 1):
            print("--------- Gráficos do Robô! ---------")
            print()
            print("Qual varivel você quer analisar?")
            print("1 - X")
            print("2 - Vx")
            print("3 - ax")
            print("4 - Y")
            print("5 - Vy")
            print("6 - ay")
            
            choice_var = int(input("--> "))
            
            if(choice_var == 1):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                print(time_interception)
                print(robo_x2)
                plt.plot(time_interception, robo_x2, color="w", linestyle="-.", label="Posição X")

                # Título e nome dos eixos
                plt.title("Gráfico da posição X do robô pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("X (m)")

                # Mostra o gráfico
                plt.show()
                
            elif(choice_var == 2):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                plt.plot(time_interception, robo_vx, color="w", linestyle="-.", label="Velocidade X")

                # Título e nome dos eixos
                plt.title("Gráfico da velocidade X do robô pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("VX (m/s)")

                # Mostra o gráfico
                plt.show()
                
            elif(choice_var == 3):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                plt.plot(time_interception, robo_ax, color="w", linestyle="-.", label="Aceleração X")

                # Título e nome dos eixos
                plt.title("Gráfico da aceleração X do robô pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("AX (m/s^2)")

                # Mostra o gráfico
                plt.show()
                
            elif(choice_var == 4):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                plt.plot(time_interception, robo_y2, color="w", linestyle="-.", label="Posição Y")

                # Título e nome dos eixos
                plt.title("Gráfico da posição Y do robô pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("Y (m)")

                # Mostra o gráfico
                plt.show()
                
            elif(choice_var == 5):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                plt.plot(time_interception, robo_vy, color="w", linestyle="-.", label="Velocidade Y")

                # Título e nome dos eixos
                plt.title("Gráfico da velocidade Y do robô pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("VY (m/s)")

                # Mostra o gráfico
                plt.show()
                
            elif(choice_var == 6):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                plt.plot(time_interception, robo_ay, color="w", linestyle="-.", label="Aceleração Y")

                # Título e nome dos eixos
                plt.title("Gráfico da aceleração Y do robô pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("AY (m/s^2)")

                # Mostra o gráfico
                plt.show()
                
        
        elif(choice_obj == 2):
            print("--------- Gráficos da Bola! ---------")
            print()
            print("Qual varivel você quer analisar?")
            print("1 - X")
            print("2 - Vx")
            print("3 - ax")
            print("4 - Y")
            print("5 - Vy")
            print("6 - ay")
            choice_var = int(input("-> "))
            
            if(choice_var == 1):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                plt.plot(time_interception, bola_x2, color="w", linestyle="-.", label="Posição X")

                # Título e nome dos eixos
                plt.title("Gráfico da posição X da bola pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("X (m)")

                # Mostra o gráfico
                plt.show()
                
            elif(choice_var == 2):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                plt.plot(time_interception, bola_vx, color="w", linestyle="-.", label="Velocidade X")

                # Título e nome dos eixos
                plt.title("Gráfico da velocidade X da bola pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("VX (m/s)")

                # Mostra o gráfico
                plt.show()
                
            elif(choice_var == 3):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                plt.plot(time_interception, bola_ay, color="w", linestyle="-.", label="Aceleração X")

                # Título e nome dos eixos
                plt.title("Gráfico da aceleração Y da bola pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("AY (m/s^2)")

                # Mostra o gráfico
                plt.show()
                
            elif(choice_var == 4):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                plt.plot(time_interception, bola_y2, color="w", linestyle="-.", label="Posição Y")

                # Título e nome dos eixos
                plt.title("Gráfico da posição Y da bola pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("Y (m)")

                # Mostra o gráfico
                plt.show()
                
            elif(choice_var == 5):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                plt.plot(time_interception,bola_vy, color="w", linestyle="-.", label="Velocidade Y")
                plt.legend()
                # Título e nome dos eixos
                plt.title("Gráfico da velocidade Y da bola pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("VY (m/s)")

                # Mostra o gráfico
                plt.show()
                
            elif(choice_var == 6):
                ax = plt.axes() 
                ax.set_facecolor("grey")
                plt.plot(time_interception, bola_ay, color="w", linestyle="-.", label="Aceleração Y")

                # Título e nome dos eixos
                plt.title("Gráfico da aceleração Y da bola pelo tempo.")
                plt.xlabel("Tempo (t)")
                plt.ylabel("AY (m/s^2)")

                # Mostra o gráfico
                plt.show()
                
        elif(choice_obj == 3):
            ax = plt.axes() 
            ax.set_facecolor("grey")
            plt.plot(robo_x2, robo_y2,  color='w',linestyle=":", label="robo")
            plt.plot(bola_x2, bola_y2,  color='r',linestyle="--", label="bola")
            plt.legend()
            plt.plot(robo_x2[-1], robo_y2[-1])
            plt.plot(bola_x2[-1], bola_y2[-1])

            # Título e nome dos eixos
            plt.title("Gráfico da trajetória da bola e do robô no campo.")
            plt.xlabel("X")
            plt.ylabel("Y")

            # Mostra o gráfico
            plt.show()
        elif(choice_obj == 4):
            ax = plt.axes() 
            ax.set_facecolor("grey")
            plt.plot(time_interception,dist_euclidiana, color="w", linestyle="-.", label="Distância D")
            plt.legend()
            # Título e nome dos eixos
            plt.title("Gráfico da distancia entre o Robo e a Bola pelo Tempo.")
            plt.xlabel("Tempo (t)")
            plt.ylabel("Distância")

            # Mostra o gráfico
            plt.show()
            
        elif(choice_obj == 0):
            print("Obrigado por usar os serviços da OrangoCorps!")
            break
        else:
            print("Opção inválida.")