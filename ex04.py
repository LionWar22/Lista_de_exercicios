
# v = float(input("Velocidade em km/h: "))
#
# t = float(input("Tempo em h : "))
#
# s = v * t
#
# print("Distancia de {} Km".format(s))

#Aperfeiçoando o exercicio


def calcDistancia(): #Função calcula a distancia
    v = float(input("Velocidade em km/h: "))  #As variaveis necessarias para o calculo são criadas dentro das funções
    t = float(input("Tempo em H: "))
    print("Distancia: {} Km" .format(v * t))  # A impressão do resultado ocorre dentro da função

def calcVelocidade(): #Função calcula a velocidade
    t = float(input("Tempo em H: "))
    s = float(input("Distancia em Km: "))
    print("Velocidade: {} km/h".format( s / t ))

def calcTempo(): #Função calcula o Tempo
    v = float(input("Velocidade em km/h: "))
    s = float(input("Distancia em Km: "))
    print("Tempo: {} H".format( s / v ))

opcao = int(input("[1]Calcular Distancia \n[2]Calcular Tempo \n[3]Calcular Velocidade  \nDigite sua escolha:")) #Uma variavel armazena a opção do usuario

if 1 == opcao: #Verifica qual opção o usuario escolhe e chama a função
    calcDistancia()
elif opcao == 2:
     calcTempo()
else:
     calcVelocidade()

