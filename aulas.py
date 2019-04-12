from db_conn import ConexionBD

class Aulas:
    def __init__(self):
        self.cod = 0 
        self.nombre = '' 
        self.ubicacion = ''
        self.activo = 0
        self.db = ConexionBD()

    def leer_registros(self):
        # Traer todos los registros de la tabla
        query = 'SELECT * FROM AULAS WHERE ACTIVO=1'
        return self.db.ejecutar(query)

    