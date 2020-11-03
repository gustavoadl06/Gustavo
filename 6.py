
vertices = []

arestas = []

matriz = []

class Grafo:
    def __init__(self, no, noAux, prioridade):

        self.no = no
        self.noAux = noAux
        self.prioridade = prioridade

grafo = open('arquivomatriz.txt', 'r')

for i in grafo:

    linha = i.split()

    arestas.append(Grafo(int(linha[0]), int(linha[1]), int(linha[2])))

grafo.close()

def Inserir(vector):

    inserido = False

    for i in range( len(vertices) ):

        if (vector == vertices[i]):

            inserido = True
            break

    return inserido


for i in range( len(arestas) ):

    if(not Inserir(arestas[i].no)):

        vertices.append(arestas[i].no)

    if(not Inserir(arestas[i].noAux)):

        vertices.append(arestas[i].noAux)
vertices = sorted(vertices)


for i in range( len(vertices) ):  #Preenche matriz com 0's

    linha = []

    for j in range( len(vertices) ):

        linha.append(0)

    matriz.append(linha)


for i in range( len(arestas) ):   # matriz adjacente

    matriz[arestas[i].no][arestas[i].noAux] = arestas[i].prioridade
    matriz[arestas[i].noAux][arestas[i].no] = arestas[i].prioridade


print()
print("Matriz Adja: ")

for i in range( len(matriz) ):

    print(matriz[i])

print()


print("O grau de cada vértice é: ")

for i in range( len(matriz) ):

    g = 0

    for j in range( len(matriz[i]) ):

        if(matriz[i][j] != 0):

            g += 1
            
    print('grau do {}: {}'.format(i,g) )