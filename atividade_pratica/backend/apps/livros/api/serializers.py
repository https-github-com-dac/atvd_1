from rest_framework.serializers import ModelSerializer

from .. import models


class LivroSerializer(ModelSerializer):
    class Meta:
        model = models.Livro
        fields = "__all__"


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = models.Editora
        fields = "__all__"
