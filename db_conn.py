#Libreria de acceso a SQL_SERVER
import pyodbc 

# Defino la clase que utilizo para establer la conexion y acceso a la base de datos


class ConexionBD:
    def __init__(self, server='10.8.65.2', database='PERSONAL', usuario='sa', password='servidor'):
        self.server = server
        self.database = database
        self.usuario = usuario
        self.password = password

    def conectar(self):
        #CREA CONEXION CON LA BASE DE DATOS
        self.db = pyodbc.connect('DRIVER={SQL Server};SERVER='+self.server +
                                 ';DATABASE='+self.database+';UID='+self.usuario+';PWD='+self.password)

    def abrir_cursor(self):
        #"""Abrir un Cursor"""
        self.cursor = self.db.cursor()

    def ejecutar_consulta(self, query, values=''):
        #Ejecucion de consultas en la base de datos
        if values != '':
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
    
    def traer_datos(self):
        #Traer los datos devueltos por la consulta
        try :
            self.rows = self.cursor.fetchall()
        except:   
            self.rows = ""

    def enviar_commit(self, query):
        sql = query.lower()
        es_select = sql.count('select')
        if es_select < 1:
            self.db.commit()
            

    def cerrar_cursor(self):
        #Cerrar el cursor
        self.cursor.close()

    def ejecutar(self, query, values=''):
        # Compilar todos los procesos
        if (self.server and self.usuario and self.password and self.database and query):
            self.conectar()
            self.abrir_cursor()
            self.ejecutar_consulta(query, values)
            self.enviar_commit(query)
            self.traer_datos()
            self.cerrar_cursor()
            return self.rows
