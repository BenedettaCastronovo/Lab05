from database.DB_connect import DBConnect
from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente

class Dao:

    @staticmethod
    def iscrivi(matricola, corso):
        cnx = get_connection()
        cursor = cnx.cursor()
        query = "INSERT INTO iscrizione(matricola, codins) VALUES (%s, %s)"
        try:
            cursor.execute(query, (matricola, corso))
            cnx.commit()
            print("Iscrizione effettuata")
        except:
            print("Studente già iscritto al corso selezionato")
        cursor.close()
        cnx.close()
