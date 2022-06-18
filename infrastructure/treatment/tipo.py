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
                        'tipo_id': t[0],
                        'tipo_nm': t[1],
                        'tipo_ds': t[2]
                    }
                )
            else:
                return 404
        
        return json_tipo



