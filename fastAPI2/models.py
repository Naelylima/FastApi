from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):

    @validator('nome')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError ('Titulo precisa ter ao menos 3 palavras') #return pro HTTP
        return value

    id: Optional[int] = None
    nome: str
    aulas: str
    horas: int
    instrutor: str