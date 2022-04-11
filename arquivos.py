def escrever(novo):
    arquivo = open('arquivos.txt', 'w')
    arquivo.write(novo + "\n")

def ler():
    arquivo = open('arquivos.txt', 'r')
    return arquivo.read()

def adicionar(adici):
    arquivo = open('arquivos.txt', 'a')
    arquivo.write(adici + '\n')
