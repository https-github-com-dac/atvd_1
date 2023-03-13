from rest_framework.viewsets import ModelViewSet

from . import serializers
from .. import models


class LivroViewSet(ModelViewSet):
    queryset = models.Livro.objects.all()
    serializer_class = serializers.LivroSerializer


class EditoraViewSet(ModelViewSet):
    queryset = models.Editora.objects.all()
    serializer_class = serializers.EditoraSerializer
