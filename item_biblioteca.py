class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano):
        self.__codigo = codigo
        self.set_titulo(titulo)
        self.set_ano(ano)
        self.__disponivel = True
    
    def get_codigo(self):
        return self.__codigo