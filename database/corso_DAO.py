from database.DB_connect import DBConnect
from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente


class Dao:

    @staticmethod
    def getAllCorsi():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM corso"
        cursor.execute(query)

        corsi = []
        for row in cursor:
            corsi.append(Corso(
                codins = row["codins"],
                crediti = row["crediti"],
                nome = row["nome"],
                pd=row["pd"],
                #studenti= row["studenti"],
            ))

        cursor.close()
        cnx.close()
        return corsi

    @staticmethod
    def getStudentiCorso(codice):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT s.* FROM studente s
                JOIN iscrizione i ON s.matricola = i.matricola
                WHERE i.codins= %s"""
        cursor.execute(query, (codice,))

        studentiCorso = []
        for row in cursor:
            studentiCorso.append(Studente(
                matricola= row["matricola"],
                nome= row["nome"],
                cognome= row["cognome"],
                CDS = row["CDS"],
            ))

        cursor.close()
        cnx.close()
        return studentiCorso