numeros = [1, 2, 2, 3, 1, 4, 3, 5]

sem_duplicatas = []

for n in numeros:
    if n not in sem_duplicatas:
        sem_duplicatas.append(n)

print(sem_duplicatas)