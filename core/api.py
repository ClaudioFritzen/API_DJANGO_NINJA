from ninja import NinjaAPI

from treino.api import treino_router

api = NinjaAPI(title="API Django Ninja", version="1.0.0 ")


api.add_router('/', treino_router)