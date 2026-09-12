class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3, nota4, nota5):

         self.matricula = matricula
         self.nome = nome
         self.nota1 = nota1
         self.nota2 = nota2
         self.nota3 = nota3
         self.nota4 = nota4
         self.nota5 = nota5

aluno1 = Aluno(201030,"Sam", 6.0, 8.0, 9.5, 7.8, 9.1)
aluno2 = Aluno(201031,"Bem", 5.0, 7.0, 8.0, 7.0, 9.0)

print(aluno1 __dict__)
