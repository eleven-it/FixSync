from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)  # Obligatorio
    telefono = serializers.CharField(min_length=8, max_length=15, required=False)

    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_nombre(self, value):
        """ Validar que el nombre no sea vacío y tenga más de 2 caracteres """
        if len(value.strip()) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return value

    def validate_email(self, value):
        """ Validar que el email sea único """
        if Cliente.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está registrado.")
        return value    
