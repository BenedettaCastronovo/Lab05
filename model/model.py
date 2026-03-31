from database import corso_DAO
from database import studente_DAO
from database import iscrizione_DAO

class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        return corso_DAO.Dao.getAllCorsi()

    def getIscrittiCorso(self, corso):
        return corso_DAO.Dao.getStudentiCorso(corso.codins)

    def cercaStudente(self, matricola):
        return studente_DAO.Dao.cercaStudent(matricola)

    def getCorso(self, matricola):
        return studente_DAO.Dao.getCorso(matricola)

    def iscrivi(self, matricola, corso):
        iscrizione_DAO.Dao.iscrivi(matricola, corso.codins)
