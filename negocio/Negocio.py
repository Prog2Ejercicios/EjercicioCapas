import data.DBConnection as dbc


class Cliente(object):

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni 
    
    def guardar(self):
        #todo
        pass

    def __str__(self):
        return ('{} {} {}'.format(self.nombre, self.apellido, self.dni))

class Negocio(object):

    def __init__(self):
        self.db_conn = dbc.DBConnection()

    def get_cliente_by_dni(self, dni):
        query = 'SELECT * FROM cliente Where dni = {}'.format(dni)
        try:
            result = self.db_conn.fetchone(query)
            cliente = Cliente(result[0], result[1], result[2])
            print(cliente)
            return cliente
        except Exception as e:
            print('Error al obtener cliente {}'.format(e))
            return None
    
    def get_clientes(self):
        """Consulta todos los clientes y los devuelve"""
        #todo
        pass