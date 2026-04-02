class Persona:
    def __init__(self,nome,cognome,eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta

    def __str__(self):
        return f"Il mio nome è {self.nome} {self.cognome} ho {self.eta} anni!"

class Dottore(Persona):
    def __init__(self, nome, cognome, eta,specializzazione,stipendio):
        super().__init__(nome, cognome, eta)
        self.specializzazione=specializzazione
        self.stipendio=stipendio
    
    def __str__(self):
        return super().__str__()+f" Sono specializzato in {self.specializzazione} stipendio: {self.stipendio}"
    

class Paziente(Persona):
    def __init__(self, nome, cognome, eta,gruppo_sanguigno,patologie):
        super().__init__(nome, cognome, eta)
        self.gruppo=gruppo_sanguigno
        self.patologie=patologie

    def __str__(self):
        return super().__str__()+f"gruppo sanguigno:({self.gruppo}) e le mie patologie sono: {self.patologie}"

patologie=["febbre","tosse"]

d= Dottore("Marco","Marchese",40,"Chirurgia",2500)
p = Paziente("Livio","Pazzo",33,"A",patologie)

print("------------------")
print(d)
print(p)
print("------------------")
