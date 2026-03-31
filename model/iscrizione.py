from dataclasses import dataclass

@dataclass
class Iscrizione:
    matricola: int
    codins: str

    def __str__(self):
        return f'{self.matricola} iscritta al corso: {self.codins}'

    def __hash__(self):
        return hash((self.matricola, self.codins))

    def __eq__(self, other):
        return (self.matricola, self.codins) == (other.matricola, other.codins)