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

    def get_jonge_landen(self, vanaf_jaar):
        """Haal landen op die onafhankelijk zijn geworden na een bepaald jaar."""

        query = "SELECT name, indepYear FROM country WHERE indepYear > %s"
        
        try:
            with self.connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, (vanaf_jaar,))
                    return cursor.fetchall()
        except Error as e:
            print(f"Fout bij ophalen van gegevens: {e}")
            return []
