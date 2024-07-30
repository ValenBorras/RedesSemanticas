from icecream import ic
from attrs import define, field
from enum import Enum, auto

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
    x = Concepto("Perro")
    y = Concepto("Animal")

    x.relacionar(y, Relacion.ES)    

    ic(x.relaciones)