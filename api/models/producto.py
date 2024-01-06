from pydantic import BaseModel

class Producto(BaseModel):

    id: int
    nombre: str
    descripcion: str
    precio: float
    cantidad: int
    fecha_creacion: str
    fecha_actualizacion: str
    estado: str
    id_usuario: int