
nAlunos = 10 #Aqui se pode fazer um Input e solicitar do usuario o valor
idade = 0

for x in range(0,nAlunos):
    idade += int(input("Idade Aluno {} :".format(x+1)))

media = idade/nAlunos

print("Media de idade dos alunos: {}".format(media))
