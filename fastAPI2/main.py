from fastapi import FastAPI
from fastapi import HTTPException, status
from fastapi import Response
from models import Curso
from fastapi import Path, Query, Header, Depends
from typing import Optional, Any, Dict
from time import sleep

app = FastAPI(
    title='API da ETS',
    version='1.0',
    description='API desenvolvida em aula',

)
def fake_bd():
    try: 
        print("Abrindo conexão com o banco de dados!")
        sleep(1)
    finally:
        print('Fechando conexão com o banco de dados')
        sleep(1)

@app.get('/cursos', description='Retorna todos os cursos ou uma listavazia', summary='Retorna tudo!', response_model=Dict[int, Curso])
async def get_cursos(db: Any = Depends(fake_bd)):
    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int = Path(default=None, title='Id do Curso', description='deve estar entre 1 e2', gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso Não Encontrado.')

cursos = {
    1: {
        "nome": "Curso de Python",
        "aulas": 20,
        "horas": 80,
        "instrutor": "Cleber"
    },
    2: {
        "nome": "Curso de Java",
        "aulas": 15,
        "horas": 60,
        "instrutor": "Leonardo"
    }
}
@app.get('/calculadora')
# = Query(default=None, gt=5) 
async def calcular(a:int= Query(default=None, gt=5),b : int= Query(default=None, gt=10), xteste: str=Header(default=None),c: Optional[int]=0):
    soma = a+b+c
    print(f'X_TEST: {xteste}')
    return {"Resultado": soma}

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    k = None
    for key in cursos.keys():
        k = key
    next_id = k + 1
    if curso.id not in cursos:
        cursos[next_id] = curso
        cursos[next_id].id = next_id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Já existe um curso com o ID {curso.id}')

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Esse Curso Não Existe.")


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        #return JSONResponse(status_code = status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Esse Curso Não Existe.")




if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="info", reload=True)
