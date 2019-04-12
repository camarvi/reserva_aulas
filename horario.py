from db_conn import ConexionBD

class Horario:
    def __init__(self):
        self.cod = 0
        self.nombre = '' 
        self.db = ConexionBD()

    def leer_registros(self):
        query = "SELECT * FROM HORARIO_RESERVA"
        return self.db.ejecutar(query)
