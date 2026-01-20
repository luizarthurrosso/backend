from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/tarefas")
async def tarefa():
  return {"message": "Tarefa 01"}