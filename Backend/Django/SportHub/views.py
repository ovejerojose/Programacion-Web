from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model


class LoginView(APIView):
    permission_classes=[AllowAny]
    #queryset = get_user_model().objects.all()
    def post(self,request):
        #Reciéra,ps ñas credemcoañes y autenticamos al usuario:
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
    
#Si es correcto añadimos a la request la informacion de sesion:

class SignupView(generics.CreateAPIView):
    #queryset = get_user_model().objects.all()
    serializer_class=UserSerializer