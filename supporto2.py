class Gatti:
    razza=""
    età:int 
    nome=""
    def descrive(self):
        descrizione="Il gatto %s è di razza %s e ha %d anni" % (self.nome,self.razza,self.età)
        return descrizione
def moltiplicazione(x,y):
         return(x*y)