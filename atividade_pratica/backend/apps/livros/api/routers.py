from rest_framework.routers import DefaultRouter

from . import viewsets

livro_editora = DefaultRouter()

livro_editora.register(r"livros", viewsets.LivroViewSet, basename="api-livros")
livro_editora.register(r"editoras", viewsets.EditoraViewSet, basename="api-editoras")
