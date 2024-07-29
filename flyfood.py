arquivos_coordenadas = open("coordenadas.txt", "r")
texto = arquivos_coordenadas.readlines()
arquivos_coordenadas.close()

matriz = []
pontos_entrega = {}
permut = []

for linha in texto:
    matriz.append(linha.split())

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] != "0":
            pontos_entrega[matriz[i][j]] = (i, j)
pontos_ordenados = [ponto for ponto in pontos_entrega if ponto != "R"]


def gerar_permutacao(lista):
    if len(lista) == 1:
        return [lista]
    permutacao = []
    for i, elemento in enumerate(lista):
        lista_sem_elemento = lista[:i] + lista[i + 1:]
        permutacao_sem_elemento = gerar_permutacao(lista_sem_elemento)
        for p in permutacao_sem_elemento:
            permutacao.append([elemento] + p)
    return permutacao

# adiciona o R de volta a permutação
perm = gerar_permutacao(pontos_ordenados)
for per in perm:
    permutacao_completa = ["R"] + per + ["R"]
    permut.append(permutacao_completa)
    print(permutacao_completa)


def calculo_distancia(coordenadas, rotas_permutadas):
    menor_custo = float("inf")
    melhor_caminho = " "
    for r in rotas_permutadas:
        custo_total = 0
        for i in range(len(r)- 1):
            xa, ya = coordenadas[r[i]]
            xb, yb = coordenadas[r[i + 1]]
            custo_total += abs(xa - xb) + abs(ya - yb)
        if custo_total < menor_custo:
            menor_custo = custo_total
            melhor_caminho = " ".join(r)
    return f"A menor rota seria {melhor_caminho}, custando um total de {menor_custo} drônometros"


dist = calculo_distancia(pontos_entrega, permut)
print(dist)
