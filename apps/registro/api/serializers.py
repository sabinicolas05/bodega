from rest_framework.serializers import ModelSerializer
from apps.registro.models import PostRegistro

class  RegisSerializer(ModelSerializer):
    class Meta:
        model = PostRegistro
        fields = ['id','nombre', 'categoria','cantidad','fecha_salida' ]