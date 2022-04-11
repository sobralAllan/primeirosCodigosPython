import this

guardarNome = ""
guardarTelefone = ""
guardarEndereco = ""
guardarDataDeNascimento = ""

def cadastrar(nome, telefone, endereco, dataDeNascimento):
    this.guardarNome = nome
    this.guardarTelefone = telefone
    this.guardarEndereco = endereco
    this.guardarDataDeNascimento = dataDeNascimento

def retornarNome():
    return this.guardarNome

def retornarTelefone():
    return this.guardarTelefone

def retornarEndereco():
    return this.guardarEndereco

def retornarDataDeNascimento():
    return this.guardarDataDeNascimento

def imprimir():
    print('Nome é {}, \ntelefone: {}, \nendereço: {}, \nData de Nascimento: {}'.format(retornarNome(), retornarTelefone(), retornarEndereco(), retornarDataDeNascimento()))