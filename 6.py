import heapq


class Tarefas: 
    def __init__ (self, desc, prior):
        self.desc=desc
        self.prior=prior
    def setDesc(self,desc):
        self.desc=desc
    def getDesc(self):
        return self.desc
    def setPrior(self, prior):
        self.prior=prior
    def getPrior(self):
       return self.prior



lista=[]
for i in range (0,3):
    descTarefa=input('Digite a descrição da tarefa {}: '.format(i+1))
    priorTarefa=int(input('Digite a prioridade da tarefa {}: '.format(i+1)))
    Tarefa =Tarefas(descTarefa,priorTarefa)
    heapq.heappush(lista,(Tarefa.prior, Tarefa.desc))
    
for i in range (0,3):
    print(heapq.heappop(lista))