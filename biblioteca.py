class biblioteca:
    def __init__(self):
        self._itens = []

    def adicionar_item(self, item):
        self._itens.append(item)
        print(f"item'{item.get_titulo()}' adicionado com sucesso !")
    
    def listar_itens(self):
        if not self.__itens:
            print("Nenhum item cadastrado.")
        for item in self.__itens:
            item.exibir_detalhes()
    
    def buscar_por_codigo(self, codigo):
        for item in self.__itens:
            if item.get_codigo() == codigo:
                return item
        return None
    
    def emprestar_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            item.emprestar()
        else:
            print(f"Item com código {codigo} não encontrado.")
    
