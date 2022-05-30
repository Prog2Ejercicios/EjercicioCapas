import sqlite3

class DBConnection(object):
    """Clase para conexion de db sqlite3"""
    DB_LOCATION = "db.sqlite"

    def __init__(self):
        self.__connection = sqlite3.connect(DBConnection.DB_LOCATION)
        self.__cur = self.__connection.cursor()
        self.__create_tables()

    def __create_tables(self):
        """Crea las tablas"""
        self.__cur.execute('''CREATE TABLE IF NOT EXISTS cliente(nombre text,
                                                            apellido text,
                                                            dni text PRIMARY KEY
                                                            )''')
        try:
            self.__cur.execute(''' INSERT INTO cliente VALUES('Dummy', 'Cliente', '123456')''')
        except:
            pass
        #todo: crear tabla de productos
        self.commit()

    def __execute(self, query):
        self.__cur.execute(query)

    def fetchone(self, query):
        self.__execute(query)
        return self.__cur.fetchone()

    def fetchall(self, query):
        #todo
        pass

    def commit(self):
        self.__connection.commit()

    def close(self):
        self.__connection.close()

    def __del__(self):
        self.__connection.close()