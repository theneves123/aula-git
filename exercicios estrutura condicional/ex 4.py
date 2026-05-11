#Exercício 4: Sistema de Notas
#Peça ao usuário que digite uma nota (use float() ).
#● Se a nota for maior ou igual a 9.0, exiba: "Parabéns!! Você foi aprovado!".
#● Se a nota for entre 7.0 e 8.9, exiba: "Aprovado.".
#● Se a nota for entre 4.0 e 6.9, exiba: "Em Recuperação".
#● Caso seja menor que 4.0, exiba: "Reprovado".

nota = float(input("digite a sua nota: "))

if nota >= 9:
    print("Parabens você foi aprovado!!!")
elif nota >= 7:
    print("Aprovado")
elif nota >= 4:
    print("Recuperação")
else:
    print("Reprovado")

