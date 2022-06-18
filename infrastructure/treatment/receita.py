from infrastructure.database.postgre import PostgreSQL

class Receita():
    def __init__(self):
        self.table = 'receitas'
        self.postgre = PostgreSQL()

    def create_receita(self,name, descricao, valor, date, categoria, tipo):
        pass

    def update_receita(self):
        pass

    def remove_receita(self):
        pass

    def list_receita(self):
        tuplas = self.postgre.select(self.table)

        json_receita = []

        for t in tuplas:
            if len(t) == 7:
                json_receita.append(
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
        
        return json_receita