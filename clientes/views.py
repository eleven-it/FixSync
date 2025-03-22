from django.shortcuts import render

from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.filter(activo=True)  # Solo clientes activos
    serializer_class = ClienteSerializer  # Usamos el serializador
    filter_backends = [filters.SearchFilter]
    ordering_fields = ['nombre', 'fecha_registro']  # Permite ordenar por estos campos    
    search_fields = ['nombre', 'email']  # Permite buscar clientes por nombre o email
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder
    
    def destroy(self, request, *args, **kwargs):
        """En lugar de eliminar el cliente, lo desactivamos"""
        cliente = self.get_object()
        cliente.activo = False
        cliente.save()
        return Response({"mensaje": "Cliente desactivado"}, status=status.HTTP_204_NO_CONTENT)
