a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

intersecao = []

for i in a:
    if i in b and i not in intersecao:
        intersecao.append(i)

print(intersecao)