
from django.urls import path
from .views import LoginView, LogoutView,SignupView,AddProductView,AddCourtView

urlpatterns=[
    #Auth views
    path('auth/login/',LoginView.as_view(),name='auth_login'),
    path('auth/logout/',LogoutView.as_view(),name='auth_logout'),
    path('auth/signup/',SignupView.as_view(),name='auth_signup'),
    path('add/products/',AddProductView.as_view(),name='Add_products'),
    path('add/court/',AddCourtView.as_view(),name='Add_court'),
    ]