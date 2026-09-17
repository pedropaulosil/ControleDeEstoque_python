class Produto:
    def __init__(self, nome: str, quantidade: int):
        self._nome = nome
        self._quantidade = quantidade
    # Atributos Produto
    # Getters 
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def quantidade(self) -> int:
        return self._quantidade

    # Setters
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self._quantidade = quantidade
