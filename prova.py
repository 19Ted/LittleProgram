class CarClass:
    name=""
    kind=""
    color=""
    price=""
    def description(self):
        descrizione="L'auto di nome %s è %s di colore %s e costa %s" % (self.name,self.kind,self.color,self.price)
        return descrizione

macchina1=CarClass()
macchina1.name="Ladro"
macchina1.kind="un trattore"
macchina1.color="arcobaleno"
macchina1.price="2 miliardi di euro"

macchina2=CarClass()
macchina2.name="Shrek"
macchina2.kind="una spider"
macchina2.color="viola"
macchina2.price="50 cent"

print(macchina1.description())
print(macchina2.description())