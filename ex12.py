
velocidade = 110
distancia = 640
partida = 20

tempo = distancia/velocidade #CAlcula tempo

chegada = partida + tempo #Calcula chegada

while (chegada >= 24):       #Laço de repetição que sertifica de a chegada estar entre 0 e 23h
    chegada = (partida + tempo) - 24 #Enquanto a hora de chegada é maior que 24h se subtrai 24 para ter a hora real

if (chegada - int(chegada)) >= 0.60:        # Aqui tratamos os minutos, para aparecer entre 0.00 e 0.59 e não valores maiores como 0.82
    minutos = (chegada - int(chegada) - 0.60)    #Aqui salvamos numa variavel os minutos a mais depois de 0.60 (que é uma hora)
    chegada = (chegada - (chegada - int(chegada)) + 1 + minutos) #Então somamos a hora a mais (Passou de 0.60 no if) e depois os minutos separados anteriormente


print("Hora de partida: {:.2f}".format(partida))
print("Tempo de duração: {:.2f}".format(tempo))
print("Hora de chegada: {:.2f}".format(chegada))
