from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from car.models import Cars
from extensions.auth import JWTQueryParamsAuthentication

class ShoppingCars(APIView):
    def get(self,request,car_id):
        car=Cars.objects.filter(id=car_id).values()
        return Response({
            "code": 200,
            "message": "success",
            "data": {
                "list": car,
            }
        })

    def put(self,request,car_id):
        car=Cars.objects.filter(id=car_id).values()
        Goods_name = request.data.get('Goods_name')
        goods_number = request.data.get('goods_number')
        car.Goods_name=Goods_name
        car.goods_number=goods_number
        car.update(Goods_name=Goods_name,goods_number=goods_number)
        return Response({
            "code": 200,
            "message": "success",
            "data": {
                "list": car,
            }
        })


    def delete(self,request,car_id):
        car =Cars.objects.filter(pk=car_id)
        car.delete()
        return Response({
            "code": 200,
            "message": "success",
            "data": {
                "list": car,
            }
        })


class AddShoppingCars(APIView):
    def get(self,request):
        car=Cars.objects.filter().all().values()
        return Response({
            "code": 200,
            "message": "success",
            "data": {
                "list": car,
            }
        })


    def post(self,request):
        Goods_name=request.data.get('Goods_name')
        goods_number = request.data.get('goods_number')
        user_id = request.data.get('user_id')

        car = Cars.objects.create(
            Goods_name=Goods_name,
            goods_number=goods_number,
            user_id=user_id,
        )
        return Response({
            "code": 200,
            "message": "success",
            "data": {
                "carId": car.id
            }
        })
