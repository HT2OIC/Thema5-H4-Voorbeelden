# domeinlogica.py
from een_een_datalaag import Datalaag  # Importeren van de datalaag

class Domeinlogica:
    def __init__(self, datalaag):
            self.datalaag = datalaag

    def toon_landen(self):
        """Landen van Europa opvragen uit de datalaag en printen."""
        continent = "Europe"
        landen = self.datalaag.get_landen_op_continent(continent)
        if landen:
            print("Lijst van landen:")
            for land in landen:
                print(f"{land[0]} {land[1]}")
        else:
            print("Geen landen gevonden.")

# Code vanuit domeinlogica starten.
# Normaal gezien gebeurt dit vanuit de presentatielaag.
if __name__ == "__main__":
    datalaag = Datalaag()
    domein = Domeinlogica(datalaag)
    domein.toon_landen()