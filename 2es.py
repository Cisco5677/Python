class Persona:
    def __init__(self,nome,cognome,eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta

    def __str__(self):
        return f"Il mio nome è {self.nome} {self.cognome} ho {self.eta} anni!"

class Dottore(Persona):
    def __init__(self, nome, cognome, eta,specializzazione,matricola,reparto):
        super().__init__(nome, cognome, eta)
        self.specializzazione=specializzazione
        self.matricola=matricola
        self.reparto=reparto
        self.pazienti=[]
    
    def aggiungi_pazienti(self,pazienti):
        self.pazienti.append(pazienti)
    
    def __str__(self):
        return super().__str__()+f"Sono specializzato in {self.specializzazione}\n matricola: {self.matricola}\n reparto: {self.reparto}\n pazienti:{self.pazienti}"
    

class Paziente(Persona):
    def __init__(self, nome, cognome, eta,id,gruppo_sanguigno):
        super().__init__(nome, cognome, eta)
        self.gruppo=gruppo_sanguigno
        self.patologie=[]
        self.id=id
        self.alergie=[]

    def agg_patologie(self,patologie):
        self.patologie.append(patologie)

    def agg_alergie(self,alergie):
        self.alergie.append(alergie)

    def __str__(self):
        return super().__str__()+f"gruppo sanguigno:({self.gruppo}) e le mie patologie sono: {self.patologie} e allergie: {self.alergie}"


p = Paziente("Livio","Pazzo",33,1,"A")
p.agg_patologie("Diabete")
p.agg_alergie("Polline")
d = Dottore("Marco","Marchese",40,"Cardiologia",32313,"Cardiologia")
d.aggiungi_pazienti(p.nome)



while True:
    print("1. Stampa Dottori")
    print("2. Stampa Pazienti")
    print("0. Esci")
    scelta = int(input("Inserisci scelta: "))
    
    match scelta:
        case 1:
            print(d)
        case 2:
            print(p)
        case 0:
            break
