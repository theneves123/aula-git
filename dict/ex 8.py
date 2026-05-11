alunos = {
    "Ana": 8.5,
    "João": 7.0,
    "Maria": 9.2
}

nome = input("Digite o nome do aluno: ")

nota = alunos.get(nome)

if nota:
    print("Nota:", nota)
else:
    print("Aluno não encontrado.")