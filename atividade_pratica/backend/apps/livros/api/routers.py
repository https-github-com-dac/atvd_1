from rest_framework.routers import DefaultRouter

from . import viewsets

livro_router = DefaultRouter()
livro_router.register(r"livros", viewsets.LivroViewSet, basename="api-livros")

editora_router = DefaultRouter()
editora_router.register(r"editoras", viewsets.EditoraViewSet, basename="api-editoras")
