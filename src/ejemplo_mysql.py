import mysql
from attrs import define

@define(repr=False)
class MYSQLinterface:
    conn: mysql.connector
    cursor: object

    def __init__ (self) -> None:
        self.conn = mysql.connector.connect(
            user = "root",
            password = "022MySQL57",
            host = "localhost",
            database = "pruebas"
        )
        self.cursor = self.conn.cursor()

    def getAllOcurrences (self) -> list[tuple]:
        query = """
                SELECT * 
                FROM CLIENTE
                ORDER BY dni ASC
                """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getOcurrencesFilteredBy (self, condition: str) -> list[tuple]:
        query = f"""
                SELECT *
                FROM CLIENTE
                WHERE {condition}
                ORDER BY dni ASC
                """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def putNewOcurrence (self, dni: int, name_surname: str, facturation_condition: str) -> None:
        query = f"""
                INSERT INTO CLIENTE (dni, nombre_apellido, condicion_facturacion)
                VALUES ({dni}, '{name_surname}', '{facturation_condition}')
                """
        self.cursor.execute(query)
        self.conn.commit()

    def setOcurrenceAttribute (self, condition: str, setted_columnxvalue: str) -> None:
        query = f"""
                UPDATE CLIENTE SET {setted_columnxvalue}
                WHERE {condition}
                """
        self.cursor.execute(query)
        self.conn.commit()

    def _testAccessTime () -> int:
        pass