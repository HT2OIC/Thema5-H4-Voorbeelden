# domeinlogica.py
from een_drie_datalaag import Datalaag  # correcte import van de datalaag

class Domeinlogica:
    def __init__(self, datalaag):
        self.datalaag = datalaag

    def toon_jonge_landen(self):
        """Toon landen die onafhankelijk zijn geworden na een opgegeven jaar."""
        
        try:
            jaar = int(input("Geef een jaar op vanaf wanneer je een land jong noemt: "))
            if jaar < 0:
                raise ValueError("Een jaar kan niet negatief zijn.")
            
            # Vraag data op bij de datalaag
            landen = self.datalaag.get_jonge_landen(jaar)
            if landen:
                print("Lijst van landen:")
                for land in landen:
                    print(f"{land[0]} {land[1]}")
            else:
                print("Geen landen gevonden.")

        except ValueError as e:
            print(f"Ongeldige input: {e}")

# Code vanuit domeinlogica starten.
if __name__ == "__main__":
    datalaag = Datalaag()
    domein = Domeinlogica(datalaag)
    domein.toon_jonge_landen()