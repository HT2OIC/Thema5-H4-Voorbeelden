# datalaag.py
import mysql.connector
from mysql.connector import Error

class Datalaag:

    def connect(self):
        """Connectie met de database maken."""
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Str3amIT#",
            database="world"
        )

    def get_levensverwachting_op_continent(self, continent):
        """Haal de levensverwachting van landen op een bepaald continent op."""
        query = "SELECT LifeExpectancy FROM country WHERE continent = %s"

        try:
            with self.connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, (continent,))
                    return cursor.fetchall()
        except Error as e:
            print(f"Fout bij ophalen van gegevens: {e}")
            return []