from abc import ABC, abstractmethod

# 🔹 ASTRAZIONE
class Persona(ABC):
    def __init__(self, nome, eta):
        self.nome = nome
        self._eta = None
        self.set_eta(eta)

    def get_eta(self):
        return self._eta

    def set_eta(self, valore):
        if not isinstance(valore, int) or valore < 0:
            raise ValueError(f"Età non valida: {valore}")
        self._eta = valore

    @abstractmethod
    def saluta(self):
        pass   # obbliga le classi figlie a implementarlo


# EREDITARIETÀ + POLIMORFISMO
class Studente(Persona):
    def __init__(self, nome, eta, matricola, voto):
        super().__init__(nome, eta)
        self.matricola = matricola
        self.voto = voto

    def saluta(self):
        return f"Ciao sono {self.nome}, ho {self._eta} anni e la mia matricola è {self.matricola}"

class Insegnante(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.materia = materia

    def saluta(self):
        return f"Buongiorno, sono il prof {self.nome} e insegno {self.materia}"

class Bidello(Persona):
    def __init__(self, nome, eta, reparto):
        super().__init__(nome, eta)
        self.reparto = reparto

    def saluta(self):
        return f"Ciao, sono {self.nome} e lavoro nel reparto {self.reparto}"

# POLIMORFISMO (funzione generica)
def fai_salutare(persona):
    print(persona.saluta())

persone = [
    Studente("Luca", 20, "123456", 28),
    Insegnante("Russo", 45, "Informatica"),
    Bidello("Mario", 50, 2)
]

for p in persone:
    fai_salutare(p)