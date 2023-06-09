"""
URL configuration for Alquiler_de_canchas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from SportHub import views
#Api router
router=routers.DefaultRouter()
router.register('viewproducts',views.ViewProductsView,basename='view_products')
router.register('viewcourt',views.courtView,basename='view_court')

urlpatterns = [
    path('admin/', admin.site.urls),
    #Api routes
    path('api/',include('SportHub.urls')),
    path('api/',include('metodo_de_pago.urls')),
    path('api/',include(router.urls))
]

