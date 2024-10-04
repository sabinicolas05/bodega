from rest_framework.views import APIView
from rest_framework. viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.salida.models import PostSalida
from apps.salida.api.serializers import SalidSerializer

class SalidaViewSet(ViewSet):
    def list(self, request):
        serializers = SalidSerializer(PostSalida.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializers.data)
     
    def retrieve(self, request, pk=int):
        serializers = SalidSerializer(PostSalida.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=serializers.data)
    
    def create(self, request):
       serializers = SalidSerializer(data=request.data)
       serializers.is_valid(raise_exception=True)
       serializers.save()
       return Response(status=status.HTTP_200_OK, data=serializers.data)
    
    def update(self, request, pk):
        try:
            serializers = PostSalida.objects.get(pk=pk)
            serializers = SalidSerializer(serializers, data=request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(status=status.HTTP_200_OK, data=serializers.data)
        except PostSalida.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self, request, pk):
        try:
            serializers = PostSalida.objects.get(pk=pk)
            serializers = SalidSerializer(serializers, data=request.data, partial=True)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(status=status.HTTP_200_OK, data=serializers.data)
        except PostSalida.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        serializers = PostSalida.objects.get(pk=pk)
        serializers.delete()
        return Response(status=status.HTTP_200_OK)
    
            
        