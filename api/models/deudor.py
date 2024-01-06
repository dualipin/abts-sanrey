from pydantic import BaseModel

class Deudor(BaseModel):

    id: int
    nombre: str
    apellido: str
    email: str
    telefono: str
    direccion: str
    ciudad: str
    pais: str
    fecha_nacimiento: str
    fecha_creacion: str
    fecha_actualizacion: str
    estado: str
    id_usuario: int