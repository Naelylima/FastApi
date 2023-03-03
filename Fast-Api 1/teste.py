from fastapi import FastAPI
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

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("teste:app", host='127.0.0.1', port=8000, log_level="info", reload=True)


#ipconfig
#   pip freeze > requirements.txt
#decorator  atribui uma nova funcionalidade para uma função:
# função assincrona