from db_conn import ConexionBD

class Reserva:
    def __init__(self, cod, aula, fecha, actividad, horario, profesional, observacion, email):
        self.cod = cod 
        self.aula = aula
        self.fecha = fecha 
        self.actividad = actividad
        self.horario = horario
        self.profesional = profesional
        self.observacion = observacion
        self.email = email
        self.db = ConexionBD()
        self.cadena_buscar = """
            SELECT RESERVA_AULA2.COD,AULAS.NOMBRE,replace(convert(varchar, FECHA, 103), ' ', '-') AS FECHA,ACTIVIDAD,HORARIO_RESERVA.NOMBRE AS HORARIO,PROFESIONAL,OBSERVACION,EMAIL 
            FROM RESERVA_AULA2,AULAS,HORARIO_RESERVA
            WHERE RESERVA_AULA2.AULA = AULAS.COD 
            AND HORARIO_RESERVA.COD = HORARIO
            """
      
    def nueva_reserva(self):
        query ='INSERT INTO RESERVA_AULA2 (aula,fecha,actividad,horario,profesional,observacion,email) VALUES (?,?,?,?,?,?,?)'
        valores = (self.aula, self.fecha, self.actividad, self.horario, self.profesional, self.observacion, self.email)
        self.db.ejecutar(query, valores)

    def borrar_reserva(self):
        query = "DELETE FROM RESERVA_AULA2 WHERE COD=?"
        valores = (self.cod)
        self.db.ejecutar(query, valores)

    def modifica_reserva(self):
        query ='UPDATE RESERVA_AULA2 SET aula=?, fecha=?, actividad=?, horario=?, profesional=?,observacion=?, email=? WHERE cod=?'
        valores = (self.aula, self.fecha, self.actividad, self.horario, self.profesional, self.observacion, self.email, self.cod)
        self.db.ejecutar(query, valores)

    def seleciona_reserva(self):
        query = "SELECT * FROM RESERVA_AULA2 WHERE COD=?"
        valores = (self.cod)
        return self.db.ejecutar(query, valores)

    def buscar_reservas_fecha(self, fecha1, fecha2):
        query = self.cadena_buscar + " AND FECHA BETWEEN ? AND ?"
        valores =(fecha1, fecha2)
        return self.db.ejecutar(query, valores)
        

    def buscar_reservas_aula(self, aula, fecha1, fecha2):
        query = self.cadena_buscar + " AND AULA=? AND FECHA BETWEEN ? AND ?"
        valores = (aula, fecha1, fecha2)
        return self.db.ejecutar(query, valores)
    
    def busca_reserva_aula_fecha_horario(self, aula, fecha, horario):
        query = self.cadena_buscar + " AULA=? AND FECHA=? AND HORARIO=?"
        valores = (aula, fecha, horario)
        return self.db.ejecutar(query, valores)

    def buscar_reservas(self):
        query = "SELECT * FROM RESERVA_AULA2"
        return self.db.ejecutar(query)

    
