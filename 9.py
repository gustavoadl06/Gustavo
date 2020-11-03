import heapq

class Tarefas:

    def _init_ (self,descricao,prioridade):
        self.descricao = descricao
        self.prioridade = prioridade

    def getDescricao(self):
        return self.__descricao

    def setDescricao(self, descricao):
        self.__descricao = descricao

lista=[]
for i in range (0,10):

    x=input('Digite a desc. da tarefa {}: '.format(i+1))

    y=int(input('Digite a prior. da tarefa {}: '.format(i+1)))

    while y>5 or y<0:

       y=int(input('Prioridade errada: Digite algum valor de 0 a 5, por gentileza {}: '.format(i+1)))

    l=(y, x)
    heapq.heappush(lista, l)


for i in range (0, 10):

    print(lista[-i][1])

    heapq.heappop(lista)
