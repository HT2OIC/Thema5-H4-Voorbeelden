# datalaag.py #Audi0Bytes#
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

    def get_landen_op_continent(self, continent):
        """Landen van een continent uit de database halen."""

        query = "SELECT code, name FROM country WHERE continent = %s"

        try:
            with self.connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, (continent,))
                    return cursor.fetchall()

        except Error as e:
            print(f"Fout bij ophalen van gegevens: {e}")
            return []