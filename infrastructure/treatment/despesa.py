from infrastructure.database.postgre import PostgreSQL

class Despesa():
    def __init__(self):
        self.table = 'despesa'
        self.postgre = PostgreSQL()

    def create_despesa(self):
        pass

    def update_despesa(self):
        pass

    def remove_despesa(self):
        pass

    def list_all_despesa(self):
        tuplas = self.postgre.select(self.table)

        json_despesa = []

        for t in tuplas:
            if len(t) == 7:
                json_despesa.append(
                    {
                        'id': t[0],
                        'nome': t[1],
                        'descricao': t[2],
                        'valor': t[3],
                        'data':t[4],
                        'categoria':t[5],
                        'tipo':t[6]
                    }
                )
            else:
                return 404
        
        return json_despesa