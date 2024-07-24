arquivos_coordenadas = open("coordenadas.txt", "r")
texto = arquivos_coordenadas.readlines()
arquivos_coordenadas.close()

matriz = []
pontos_entrega = {}

for  linha in texto:
    matriz.append(linha.split())

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] != "0":
            pontos_entrega[matriz[i][j]] = (i, j)
print(pontos_entrega)
            

