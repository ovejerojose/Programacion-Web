import mercadopago
from decouple import config
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class ProcessPaymentAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        respuesta_pago = None
        try:
            request_values=json.loads(request.body)
            # Crear una instancia de Mercado Pago y configurar las credenciales
            mp = mercadopago.SDK(config('Token_mp'))
            # Crear los datos del pago
            datos_del_comprador = {
                    "transaction_amount": float(request_values["transaction_amount"]),
                    "token": request_values["token"],
                    "installments": int(request_values["installments"]),
                    "payment_method_id": request_values["payment_method_id"],
                    "issuer_id": request_values["issuer_id"],
                    "payer": {
                        "email": request_values["payer"]["email"],
                        "identification": {
                        "type": request_values["payer"]["identification"]["type"],
                        "number": request_values["payer"]["identification"]["number"],
                                         }
                            }
            }
            # Crear el pago en Mercado Pago
            respuesta_pago = mp.payment().create(datos_del_comprador)
            pago = respuesta_pago["response"]
            # Guardar el estado del pago en tu modelo de Payment
            estado_de_pago = {
                "id": pago["id"],
                "status": pago["status"],
                "status_detail": pago["status_detail"],
            }
            return Response(data={"body":estado_de_pago, "statusCode": respuesta_pago["status"]}, status=201)
        except Exception as e:
            # Si el método de la solicitud no es POST, mostrar el formulario de pago
            return Response(data={"body": respuesta_pago}, status=400)