from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from rest_framework import status,generics,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, Products_Serializers,court_registration_Serializers
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Productos,Cancha

#Ingreso de Usuario: 
class LoginView(APIView):
    permission_classes=[AllowAny]
    #queryset = get_user_model().objects.all()
    def post(self,request):
        #Recibimoss las credenciales y autenticamos al usuario:
        email=request.data.get('email',None)
        print(email)
        password=request.data.get('password',None)
        print(password)
        user=authenticate(email=email, password=password)
        print(user)
        # Si es correcto añadimos a la request la informacion de sesion
        if user:
            login(request,user)
            return Response(UserSerializer(user).data,status=status.HTTP_200_OK)
        #Si no es correcto devolvemos un error en la petiición
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    def post(self, request):
        #Borramos de la request la informacion de sesion:
        logout(request)
        #Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)
    
class SignupView(generics.CreateAPIView):
    #queryset = get_user_model().objects.all()
    serializer_class=UserSerializer


#Ingreso de Productos:

class ViewProductsView(viewsets.ReadOnlyModelViewSet):
    permission_classes=[AllowAny]
    queryset=Productos.objects.all()
    serializer_class=Products_Serializers

class AddProductView(APIView):
    permission_classes=[IsAdminUser]
    def post (self,request,format=None):
        serializer=Products_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Registro de Canchas
class AddCourtView(APIView):
    permission_classes=[IsAdminUser]
    def post(self,request,format=None):
        serializer=court_registration_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class courtView(viewsets.ReadOnlyModelViewSet):
    permission_classes=[AllowAny]
    queryset=Cancha.objects.all()
    serializer_class=court_registration_Serializers