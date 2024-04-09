class Pokemon:
    def __init__(self, pokemon_ordbok: dict) -> None:
        self.id: int
        self.name: str = pokemon_ordbok["name"]