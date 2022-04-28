class Summa:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        
    def suorita(self, luku):
        self._sovelluslogiikka.plus(luku)
        return self._sovelluslogiikka.tulos

class Erotus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        
    def suorita(self, luku):
        self._sovelluslogiikka.miinus(luku)
        return self._sovelluslogiikka.tulos

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        
    def suorita(self):
        self._sovelluslogiikka.nollaa()
        return self._sovelluslogiikka.tulos

class Kumoa:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        
    def suorita(self):
        self._sovelluslogiikka.kumoa()
        return self._sovelluslogiikka.tulos