import Pilha
visitados =[]

def foivisitado(alvo):
    visitado.append(alvo)


def visitado(alvo):
    if alvo in visitado:
        return True
    return False
        
def dfs(grafo,alvo):
    i = 0
    p = Pilha()
   
    p.empilha(alvo)
    
    while p is not p.vazio():
        
        alvo = p.desempilha()
        
        if alvo is not visitado(alvo):
            
            foivisitado(alvo)
            
            for filho in grafo.get[i]:
                p.empilha(filho)
            

f = open("base.txt")

grafo = f.read().split('\n')

print(grafo)
i = 0
print (dfs(grafo,3))


