arquivos_coordenadas = open("coordenadas.txt", "r")
texto = arquivos_coordenadas.readlines()
arquivos_coordenadas.close()

matriz = []
pontos_entrega = {}

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
    print(permutacao_completa)