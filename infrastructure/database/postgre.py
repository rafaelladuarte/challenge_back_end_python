import datetime
import psycopg2
import psycopg2.extras

from configparser import ConfigParser, BasicInterpolation
config = ConfigParser(interpolation=BasicInterpolation)
config.read('config.ini')

class PostgreSQL():
    def __init__(self):
        self.database = config['POSTGRESQL']['DATABASE']
        self.user = config['POSTGRESQL']['USER']
        self.password = config['POSTGRESQL']['PASSWORD']
        self.host = config['POSTGRESQL']['HOST']
        self.port = config['POSTGRESQL']['PORT']

    def select_tipo_cat(self,table):
        query = f"""
            SELECT * FROM {table}
        """
        try:

            with psycopg2.connect(
                dbname=self.database, 
                user=self.user, 
                password=self.password,
                host=self.host,
                port=self.port) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    return cursor.fetchall()


        finally:
            try:
                connection.close()
            except:
                pass
    
    def select_receita(self,table):
        query = f"""
            SELECT  FROM {table}
            
        """
        try:

            with psycopg2.connect(
                dbname=self.database, 
                user=self.user, 
                password=self.password,
                host=self.host,
                port=self.port) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    return cursor.fetchall()


        finally:
            try:
                connection.close()
            except:
                pass

