import numpy as np

funcionarios = 3
setores = 3
salario = []

for i in range(funcionarios):
    dinheiro_salario = []
    for j in range(setores):
        dinheiro = float(input(f"Digite o salário do funcionário {i+1} do setor {j+1}: "))
        dinheiro_salario.append(dinheiro)
    salario.append(dinheiro_salario)

salario_np = np.array(salario)

salario_atualizado = np.dot(salario_np, 1.10)

print("\n== Salários iniciais ==")
print(salario_np)

print("\n== Salários atualizados ==")
print(salario_atualizado)
