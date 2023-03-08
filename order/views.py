from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from order.models import Orders
from extensions.auth import JWTQueryParamsAuthentication

class OrderView(APIView):
    def get(self,request):
        order= Orders.objects.all().values()
        return Response({
        "code": 200,
        "message": "success",
        "data": {
            "list": order,
        }
    })


    def post(self, request):
        Goods_name = request.data.get('Goods_name')
        goods_number = request.data.get('goods_number')
        order_price = request.data.get('order_price')
        address = request.data.get('address')
        user_id = request.data.get('user_id')

        order = Orders.objects.create(
            Goods_name=Goods_name,
            goods_number=goods_number,
            order_price=order_price,
            address=address,
            user_id=user_id
        )
        return Response({
            "code": 200,
            "message": "success",
            "data": {
                "orderId": order.id
            }
        })


class OrderDetailView(APIView):
    def get(self, request,order_id):
        order = Orders.objects.filter(pk=order_id).values()
        return Response({
            "code": 200,
            "message": "success",
            "data": {
                "list": order,
            }
        })

    def delete(self,request,order_id):
        order =Orders.objects.filter(pk=order_id)
        order.delete()
        return Response({
            "code": 200,
            "message": "success",
            "data": {
                "list": order,
            }
        })