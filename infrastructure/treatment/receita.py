from infrastructure.database.postgre import PostgreSQL
from datetime import datetime

class Receita():
    def __init__(self):
        self.table = 'receita'
        self.postgre = PostgreSQL()

    def create_receita(self,name, descricao, valor, tipo):
        values = (name, descricao, valor, datetime.now(), tipo)
        columns = ("rec_nm","rec_ds","rec_vl","rec_dt","rec_tipo_id")
        
        self.postgre.insert(self.table,values,columns)


    def update_receita(self):
        pass

    def remove_receita(self,id):
        self.postgre.delete(self.table,"rec_id",id)

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