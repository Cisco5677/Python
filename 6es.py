class Notifiche:
    def __init__(self):
        self.__pila = []

    def arriva(self,messaggio):
        self.__pila.append(messaggio)

    def leggi(self):
        if len(self.__pila) == 0:
            print("Nessuna notifica.")
        else:
            notifica = self.__pila.pop()
            print(f"Letta: {notifica}")

    def prossima(self):
        if len(self.__pila) == 0:
            print("Nessuna notifica.")
        else:
            print(f"In cima: {self.__pila[-1]}")


n = Notifiche()

n.arriva("WhatsApp: Ciao!")
n.arriva("Gmail: Hai un nuovo messaggio")
n.arriva("Instagram: Ti hanno taggato")

n.prossima()
n.leggi()
n.leggi()
n.leggi()
n.leggi()