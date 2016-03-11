from Pilha import Pilha

visitados =[]

def foivisitado(alvo):
    
    if not visitado(alvo):
        
        visitados.append(alvo)

def visitado(alvo):
    
    if alvo in visitados:

        return True

    return False
        
def dfs(grafo,alvo):

    p = Pilha(grafo)
    
    while not p.vazia():
        if visitado(alvo):
            return alvo

        atual = p.vertice_atual()

        foivisitado(atual)
        
        arestas_vertices = p.desempilha()

        for aresta_vertice in arestas_vertices:

            if not visitado(aresta_vertice):
                foivisitado(aresta_vertice)
      

##grafo = [[1, [2, 3]], [2, [4]], [3, [6]]]

grafo = []
cont = 0
while True:
    cont = cont + 1
    op = input(str(cont)+" -> ")
    if not op:
        break
    elif op == '0':
        grafo.append([cont,[]])
    elif len(op) == 1:
        grafo.append([cont,[int(op)]])
    else:
        aux = []
        for i in range(0,len(op)):
            if i%2==0:
                aux.append(int(op[i]))
        grafo.append([cont,aux])

print(grafo)

alvo = int(input("ALVO: "))

print(dfs(grafo,alvo))
