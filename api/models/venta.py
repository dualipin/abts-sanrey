from pydantic import BaseModel

class Venta(BaseModel):

    id: int
    fecha: str
    total: float
    estado: str