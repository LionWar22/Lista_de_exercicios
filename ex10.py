print("Converte para segundos")

hora = int(input("Hora: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

segTotais = (hora * 3600) + (minutos * 60) + segundos

print("Total em segundos: {}".format(segTotais))
