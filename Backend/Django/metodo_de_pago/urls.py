from django.urls import path
from .views import ProcessPaymentAPIView

urlpatterns = [
    path('payments/create/', ProcessPaymentAPIView.as_view(), name='create_payment'),
    # Otros endpoints necesarios para tu implementación
]