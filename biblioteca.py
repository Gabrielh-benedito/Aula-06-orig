class biblioteca:
    def __init__(self):
        self._itens = []

    def adicionar_item(self, item):
        self._itens.append(item)
        print(f"Item adicionado com sucesso")
