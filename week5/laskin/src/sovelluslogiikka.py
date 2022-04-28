class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.historia = []
        self.historia.append(0)
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo
        self.historia.append(self.tulos)

    def plus(self, arvo):
        self.tulos = self.tulos + arvo
        self.historia.append(self.tulos)

    def nollaa(self):
        self.tulos = 0
        self.historia.append(self.tulos)

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def kumoa(self):
        self.historia.pop()
        self.aseta_arvo(self.historia[-1])
