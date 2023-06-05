
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Productos,Cancha
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    username=serializers.CharField(required=True)
    password=serializers.CharField(min_length=8)

    class Meta:
        model=get_user_model()
        fields=('email','username','password')
    def validate_password(self,value):
        return make_password(value)

class Products_Serializers(serializers.ModelSerializer):
    Nombre_Producto=serializers.CharField(required=True)
    Descripcion=serializers.CharField()
    Stock=serializers.IntegerField()
    Precio=serializers.IntegerField()
    class Meta:
        model=Productos
        fields=('Nombre_Producto','Descripcion','Stock','Precio')

class court_registration_Serializers(serializers.ModelSerializer):
    Suelo=serializers.CharField(required=True)  
    Cantidad=serializers.IntegerField()
    Descripcion=serializers.CharField(required=True)
    class Meta:
        model=Cancha
        fields="__all__"