# domeinlogica.py
from een_vijf_datalaag import Datalaag  # correcte import van de datalaag

class Domeinlogica:
    def __init__(self, datalaag):
        self.datalaag = datalaag

    def bereken_gemiddelde_levensverwachting(self, continent="Europe"):
        """Bereken de gemiddelde levensverwachting voor een continent."""

        # Vraag data op bij de datalaag
        landen = self.datalaag.get_levensverwachting_op_continent(continent)

        # Filter lege waarden uit en zet de levensverwachtingen in een lijst
        levensverwachtingen = [land[0] for land in landen if land[0] is not None]

        if levensverwachtingen:
            gemiddelde = sum(levensverwachtingen) / len(levensverwachtingen)
            print(f"De gemiddelde levensverwachting in {continent} is: {round(gemiddelde, 2)} jaar")
        else:
            print("Geen geldige levensverwachtingen gevonden.")

# Code vanuit domeinlogica starten.
# Normaal gezien gebeurt dit vanuit de presentatielaag.
if __name__ == "__main__":
    datalaag = Datalaag()
    domein = Domeinlogica(datalaag)
    domein.bereken_gemiddelde_levensverwachting()