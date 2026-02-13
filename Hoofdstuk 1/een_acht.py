from een_zeven_datalaag import Datalaag  # correcte import van de datalaag

class Domeinlogica:
    def __init__(self, datalaag):
        self.datalaag = datalaag

    def nieuw_land(self):
        """Vraag input van de gebruiker, transformeer data en sla op via de datalaag."""
        naam = input("Geef de naam van de stad: ")
        code = input("Geef de code van het land: ").upper()  # Transformeer naar hoofdletters
        district = input("Geef de provincie: ")
        try:
            populatie = int(input("Geef het aantal inwoners van de stad: "))
            if populatie < 0:
                raise ValueError("Populatie kan niet negatief zijn.")
            
            # Stuur de getransformeerde data door naar de datalaag
            self.datalaag.store_city(naam, code, district, populatie)
        
        except ValueError as e:
            print(f"Ongeldige input: {e}")

# Code vanuit domeinlogica starten
if __name__ == "__main__":
    datalaag = Datalaag()
    domein = Domeinlogica(datalaag)
    domein.nieuw_land()