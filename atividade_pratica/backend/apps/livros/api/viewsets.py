from rest_framework.viewsets import ModelViewSet

from . import serializers
from .. import models


class LivroViewSet(ModelViewSet):
    queryset = models.Livro.objects.all()
    serializer_class = serializers.LivroSerializer
    filterset_fields = ["titulo", "data_de_lancamento"]


class EditoraViewSet(ModelViewSet):
    queryset = models.Editora.objects.all()
    serializer_class = serializers.EditoraSerializer
    filterset_fields = ["codigo", "local_de_origem", "nome_fantasia"]
