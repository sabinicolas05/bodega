from rest_framework.serializers import ModelSerializer
from apps.salida.models import PostSalida

class  SalidSerializer(ModelSerializer):
    class Meta:
        model = PostSalida
        fields = '__all__'