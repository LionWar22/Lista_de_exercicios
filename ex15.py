
print("Calculador de area" )

def calcRetangulo():                           #Funções para cada forma geometrica principal que aparece
    base = float(input("Base: "))              #Funções pegam os valores do usuarios e retornam a area
    altura = float(input("Altura: "))
    return base * altura

def calcCirculo():
    raio = float(input("Raio: "))
    divide = int(input("Valor de divisão do circulo: ")) #Caso seja um meio circulo ou 1/4 do circulo


    return (3.14 * (pow(raio,2)))/divide

def calcTriangulo():
    base = float(input("Base: "))
    altura = float(input("Altura: "))

    return (base * altura)/2

def imprimeArea(somaArea):
    print("Total Area: {}".format(somaArea))


print('[1]Retangulo [2]Circulo [3]Triangulo [4] CALCULAR [0]Sair')

somaArea = 0

while True:                                         #Menu que enquanto o usuario continuar a calcular areas vai somando em "somaArea"
    op = int(input("Digite sua opção: "))
    if op == 1:
        somaArea += calcRetangulo()
    elif op == 2:
        somaArea += calcCirculo()
    elif op == 3:
        somaArea += calcTriangulo()
    elif op == 4:
        imprimeArea(somaArea)
    else:                                           # 0 ou qualquer numero fora dos utilizados causa a saida
        exit()
