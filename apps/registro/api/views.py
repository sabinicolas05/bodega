from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.registro.models import PostRegistro
from apps.registro.api.serializers import RegisSerializer

class RegisViewSet(ViewSet):
    def list(self, request):
        serializers = RegisSerializer(PostRegistro.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializers.data) 
    
    def retrieve(self, request, pk=id):
        serializers = RegisSerializer(PostRegistro.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=serializers.data) 

    def create(self, request):
       serializers = RegisSerializer(data=request.data)
       serializers.is_valid(raise_exception=True)
       serializers.save()
       return Response(status=status.HTTP_200_OK, data=serializers.data)
    
    def update(self, request, pk):
        try:
            serializers = PostRegistro.objects.get(pk=pk)
            serializers = RegisSerializer(serializers, data=request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(status=status.HTTP_200_OK, data=serializers.data)
        except PostRegistro.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self, request, pk):
        try:
            serializers = PostRegistro.objects.get(pk=pk)
            serializers = RegisSerializer(serializers, data=request.data,  partial=True)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(status=status.HTTP_200_OK, data=serializers.data)
        except PostRegistro.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        serializers = PostRegistro.objects.get(pk=pk)
        serializers.delete()
        return Response(status=status.HTTP_200_OK)