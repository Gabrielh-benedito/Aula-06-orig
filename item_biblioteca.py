class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano):
        self.__codigo = codigo
        self.set_titulo(titulo)
        self.set_ano(ano)
        self.__disponivel = True
    
    def get_codigo(self):
        return self.__codigo
    
    def get_titulo(self):
        return self.__titulo
    
    def get_ano(self):
        return self.__ano

    def get_disponivel(self):
        return self.__disponivel
    
    def set_titulo(self, titulo):
        if titulo.strip() == "":
            raise ValueError("Título não pode ser vazio.")
        self.__titulo = titulo

    def set_ano(self, ano):
        if ano <= 0:
            raise ValueError("Ano deve ser maior que 0.")
        self.__ano = ano
