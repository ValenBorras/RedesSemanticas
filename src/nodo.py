from icecream import ic
from attrs import define, field
from enum import Enum, auto
import mysql as ms

@define(frozen=True)
class ConceptoDAO:
    def __init_subclass__(self) -> None:
        self.conn = ms.connector.connect(
            user = "root",
            password = "022MySQL57",
            host = "localhost",
            database = "redsemantica_db"
        )
        self.cursor = self.conn.cursor()

    def eliminar():
        ...

    def añadir():
        ...

    def modificar():
        ...
    
    def seleccionar():
        ...    

    def seleccionarTodo():
        ...
    

@define(frozen=True)
class Concepto:
    etiqueta: str = field(factory=str)
    relaciones: list[tuple] = field(factory=list[tuple])

    def relacionar(self, otro: object, tipo: int) -> tuple:
        rel = (tipo, otro)
        self.relaciones.append(rel)

        return rel
    
    class Relacion(Enum):
        ES = auto()
        ESTA = auto()
        TIENE = auto()
        NO_ES = auto()
        NO_ESTA = auto()
        NO_TIENE = auto()

if __name__ == "__main__":
    x: Concepto = Concepto("Perro")
    y: Concepto = Concepto("Animal")
    z: Concepto = Concepto("Dueño")
    db: ConceptoDAO = ConceptoDAO()

    x.relacionar(y, Concepto.Relacion.ES)
    z.relacionar(y, Concepto.Relacion.ES)
    z.relacionar(x, Concepto.Relacion.TIENE)

    ic(x.relaciones)
    ic(y.relaciones)
    ic(z.relaciones)

    user_input: int = None
    conceptos: list[Concepto] = []
    mensaje = """Opciones:
              1. Nuevo Concepto
              2. Nueva Relacion
              0. Salir"""
    print(mensaje)
    user_input = int(input("Input: "))

    while 0 != user_input:
        match user_input:
            case 1:
                c = Concepto(input("Etiqueta Concepto: "))
                if c.etiqueta not in [concepto.etiqueta for concepto in conceptos]: 
                    conceptos.append(c)
                else: print("Ya existe concepto")
            case 2:
                p = lambda n, c: print(f"{n}. {c}")
                for n, c in enumerate(conceptos):
                    p(n, c) 
                conceptos[int(input("Seleccione Concepto: "))].relacionar(
                    conceptos[int(input("Seleccione Otro Concepto: "))], 
                    Concepto.Relacion.ES
                )
        print(f"Hecho\n{mensaje}")
        user_input = int(int(input("Input: ")))

    ic(conceptos)