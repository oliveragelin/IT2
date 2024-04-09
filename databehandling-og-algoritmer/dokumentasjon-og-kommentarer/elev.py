class Elev:
    """
    En klasse for elever på VGS

    attributter
        navn (str): navnet til eleven
        alder (int): alderen til eleven
        klaase (str): bokstavklassen til eleven (eks: STA)
        fag (list[str]): en liste med fagene eleven tar.

    metoder
        legg_til_fag (fag: str): legger et fag til i faglisten
        fjern_fag (fag: )
    """
    def __init__(self, navn: str, alder: str, klasse: str) -> None:
        self.navn: str = navn
        self.alder: str = alder
        self.klasse: str = klasse
        self.fag: list[str] = []
    def legg_til_fag(self, fag: str):
        self.fag.append(fag)
    
    def fjern_fag(self, fag: str):
        self.fag.remove(fag)
    
    def vis_info(self):
        print(f"{self.navn} ({self.alder})")