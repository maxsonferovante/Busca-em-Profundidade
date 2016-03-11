class Pilha(object):
    def __init__(self,grafo):

        self.dados = grafo

        self.atual = 0
 
    def empilha(self, elemento):

        self.dados.append(elemento)
 
    def desempilha(self):

        if not self.vazia():

            self.arestas_vertices = self.dados[self.atual-1]        

            return self.arestas_vertices[1]

        else: return []

    def vazia(self):

        if self.atual >( len(self.dados) - 1 ):

            return True

        return False
    
    def vertice_atual(self):
        
        if self.atual < len(self.dados):

            self.aux = self.dados[self.atual]

            self.atual = self.atual + 1

            return self.aux[0]
        
