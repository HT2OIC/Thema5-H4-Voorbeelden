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

    def store_city(self, naam, code, district, populatie):
        """
        Sla een nieuwe stad op in de database.
        Alle parameters worden veilig doorgegeven via placeholders.
        """
        query = """
            INSERT INTO city (name, countrycode, district, population)
            VALUES (%s, %s, %s, %s)
        """
        try:
            with self.connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, (naam, code, district, populatie))
                    connection.commit()
                    print(f"Stad {naam} succesvol toegevoegd.")
        except Error as e:
            print(f"Fout bij opslaan van de stad: {e}")