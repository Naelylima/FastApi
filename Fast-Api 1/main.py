from fastapi import FastAPI, HTTPException,status
from models import Curso

app = FastAPI()

cursos = {
    1: {"nome": "Python",
     "aulas": 20, "horas": 60,
      "instrutor": "Cleber"
    },
    2: {"nome": "Java",
     "aulas": 15, "horas": 60, 
     "instrutor": "Leonardo"
     },
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos(curso_id: int):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso Não Encontrado.')

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso:Curso):
    if curso.id not in cursos:
        next_id = len(cursos)+ 1
        curso.id = next_id
        cursos[next_id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existe um curso com o ID {curso.id}")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload=True)




#ipconfig
#   pip freeze > requirements.txt
#decorator  atribui uma nova funcionalidade para uma função:
# função assincrona