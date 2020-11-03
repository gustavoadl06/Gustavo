
arestas = []
vertices = []
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


def Inserir(vetor):

    inserido = False

    for i in range(len(vertices)):

        if (vetor == vertices[i]):
            inserido = True
            break
    return inserido


for i in range(len(arestas)):

    if(not Inserir(arestas[i].no)):

        vertices.append(arestas[i].no)

    if(not Inserir(arestas[i].noAux)):

        vertices.append(arestas[i].noAux)

vertices = sorted(vertices)


for i in range(len(vertices)): # Preenche a matriz com 0's
    linha = []

    for j in range(len(vertices)):

        linha.append(0)

    matriz.append(linha)



for i in range(len(arestas)): #matriz adjacente

    matriz[arestas[i].no][arestas[i].noAux] = arestas[i].prioridade
    matriz[arestas[i]
           .noAux][arestas[i].no] = arestas[i].prioridade



try: # Le o vértice
    v = int(input("Informe o vertice desejado: "))

except ValueError as vet:

    print("Erro: {}".format(vet))
    
    exit()


exist = False  #Verificar se o vértice existe

for i in range( len(vertices)):

    if v == vertices[i]:

        exist = True

        break

if exist == False:

    print("O vertice solicitado não existe")

    exit()

#Retornar os adjacentes


adj = []
for i in range(len (matriz[v]) ):
    if matriz[v][i] != 0:
        adj.append(i)
print("Os valores correspondentes aos vertices adjacentes são: ")
print(adj)