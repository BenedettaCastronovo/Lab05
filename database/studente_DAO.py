from database.DB_connect import DBConnect
from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente

class Dao:

    @staticmethod
    def cercaStudent(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM studente WHERE trim(matricola) = trim(%s)"
        cursor.execute(query, (matricola,))
        studente = cursor.fetchone()

        cursor.close()
        cnx.close()
        if not studente:
            return None, None

        return studente["nome"], studente["cognome"]

    @staticmethod
    def getCorso(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary = True)

        query = """SELECT c.* FROM corso c
                        JOIN iscrizione i ON c.codins = i.codins
                        WHERE i.matricola= %s"""

        cursor.execute(query, (matricola,))

        corsi = []
        for row in cursor:
            corsi.append(Corso(
                codins=row["codins"],
                nome=row["nome"],
                crediti=row["crediti"],
                pd=row["pd"]
            ))

        cursor.close()
        cnx.close()
        if not corsi:
            return None, None
        return corsi

