from infrastructure.database.postgre import PostgreSQL

class Categoria():
    def __init__(self):
        self.table = 'categoria'
        self.view = 'despesa_categoria'

    def list_categoria(self):
        tuplas = self.postgre.select(self.table)

        json_categoria = []

        for t in tuplas:
            if len(t) == 7:
                json_categoria.append(
                    {
                        'id': t[0],
                        'nome': t[1],
                        'descricao': t[2]
                    }
                )
            else:
                return 404
        
        return json_categoria

    