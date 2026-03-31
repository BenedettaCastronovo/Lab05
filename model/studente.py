from dataclasses import dataclass

#from model.corso import Corso


@dataclass
class Studente:
    matricola:int
    cognome: str
    nome: str
    CDS: str
    """corsi: set[Corso]"""

    def __str__(self):
        return f"{self.matricola} - {self.cognome} - {self.nome} - {self.CDS}"

    def __hash__(self):
        return hash(self.matricola)

    def __eq__(self, other):
        return self.matricola == other.matricola