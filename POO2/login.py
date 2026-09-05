"""Criar uma Classe"""
class Carro:

    def __init__(self, cor, marca, linha, combustivel): 
     self.cor = cor
     self.marca = marca
     self.linha = linha
     self.combustivel = combustivel

"""Criando um objeto"""
polo = Carro("branco", "volkswagen","polo", "gasolina")
mustang = Carro("vermelho", "ford","mustang", "gasolina")
prius = Carro("azul", "toyota", "prius", "eletrico")
golf= Carro("preto", "volkswagen", "golf", "disel")


"""Mostrando na tela"""

print(f"a cor do {prius} é: {prius.cor}")