import this
import cadastrarUsuario
this.opcao = 1
import arquivos


def menu():
    print('Escolha uma das opções abaixo: \n' +
          '1. Cadastrar\n' +
          '2. Consultar\n' +
          '3. Atualizar\n' +
          '4. Excluir\n'   +
          '0. Sair')
    this.opcao = int(input())


def operacao():
    while(this.opcao != 0):
        menu()

        if this.opcao == 1:
            print("Informe seu nome: ")
            nome = input()
            print("Informe seu telefone: ")
            telefone = input()
            print("Informe seu endereço: ")
            endereco = input()
            print("Informe sua data de nascimento: ")
            dtNascimento = input()
            # Cadastrar usuário
            cadastrarUsuario.cadastrar(nome, telefone, endereco, dtNascimento)
            print("Cadastrado com sucesso!")
        elif this.opcao == 2:
            # pular a linha
            print("Seus dados são:\n ")
            cadastrarUsuario.imprimir()
        elif this.opcao == 3:
            print('Atualizar')
            print("Atualizado com sucesso!")
        elif this.opcao == 4:
            cadastrarUsuario.cadastrar("","","","")
            print("Apagado com sucesso!")
        elif this.opcao == 0:
            print("Obrigado!")
        else:
            print("Opção selecionada não é válida!")

def tabuada(num, vezes):
    for i in range(2, vezes): #início, fim
        print('{} * {} = {}'.format(i, num, i * num))

def frutas():
    fruit = ["Maça", "Banana", "Arroz"]
    for x in fruit:
        print(x)

def coletar():
    vetor = ["0",1,5,6,8,90]
    for i in range(len(vetor)):
        arquivos.adicionar(str(vetor[i]))


if __name__ == "__main__":
    #operacao() #Chamando o método que executa a operação
    #arquivos.escrever("Allan ")
    #arquivos.escrever(coletar())
    coletar()
    print(arquivos.ler())






