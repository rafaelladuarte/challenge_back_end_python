import psycopg2
import psycopg2.extras

from configparser import ConfigParser, BasicInterpolation
config = ConfigParser(interpolation=BasicInterpolation)
config.read('~/config.ini')

class PostgreSQL():
    def __init__(self):
        self.database = config['POSTGRESQL']['DATABASE']
        self.user = config['POSTGRESQL']['USER']
        self.password = config['POSTGRESQL']['PASSWORD']
        self.host = config['POSTGRESQL']['HOST']
        self.port = config['POSTGRESQL']['PORT']
 
    def select(self,table):
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

    def insert(self,table,values,columns):

        query = f"""
            INSERT INTO {table} ({columns})
            VALUES ({values})
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

        finally:
            try:
                connection.commit()
                connection.close()
            except:
                pass

