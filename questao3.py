"""Criando uma classe pessoa"""

class Pessoa:
    def __init__(self, n, i, p, o):#Dentro dos parenteses ficam os parametros que o ususario vai fornecer

        self.nome = n #self
        self.idade = i
        self.peso = p
        self.altura = o

    def apresentacao(self):
       print(f"O nome da pessoa consultada e{self.nome};\nA idade dele(a) e:{self.idade};")

    def fazer_anivesario(self):
        self.idade = self.idade+1 #esse metodo pega a idade do objeto e soma + 1
        print(f"feliz aniversario {self.nome}!!! Sua nova idade agora e:{self.idade}.")



"""Criando os objetos da classe pessoa"""

pessoa1 = Pessoa("Sam",18,62,1.74)
pessoa2 = Pessoa("Bem",10,52,1.50)

"""Criando os metodos"""
pessoa1.apresentacao()
pessoa1.fazer_anivesario()
pessoa1.apresentacao()
