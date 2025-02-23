from ninja import Router
from .schemas import AlunoSchema

treino_router = Router()



@treino_router.post("/treino")
def get_treino(request, aluno_schema: AlunoSchema):
    print(aluno_schema.dict())
    return {"message": "Hello World"}