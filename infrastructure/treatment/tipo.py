from infrastructure.database.postgre import PostgreSQL

class Tipo():
    def __init__(self):
        self.table = 'tipo'
        self.view = 'saldo_tipo'
        self.postgre = PostgreSQL()

    def list_tipo(self):
        tuplas = self.postgre.select(self.table)

        json_tipo = []

        for t in tuplas:
            if len(t) == 3:
                json_tipo.append(
                    {
                        'id': t[0],
                        'nome': t[1],
                        'descrição': t[2]
                    }
                )
            else:
                return 404
        
        return json_tipo



