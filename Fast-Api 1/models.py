from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel): #Por padrão já herda varias coisas, como validação de dados!
    id: Optional[int]= None #Ja que é opcional
    nome: str
    aulas: int
    horas: int
    instrutor: str