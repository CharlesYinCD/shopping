from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from goods.models import Goods
from extensions.auth import JWTQueryParamsAuthentication


class GoodsView(APIView):
  authentication_classes = ()
  def get(self,request):
   goods = Goods.objects.all().values()
   return Response({
    "code": 200,
    "message": "success",
    "data": {
     "list":goods,
    }
   })

class GoodsDetailView(APIView):
 authentication_classes = ()
 def get(self,request,goods_id):
  goods= Goods.objects.filter(pk=goods_id).values()
  return Response({
   "code": 200,
   "message": "success",
   "data": {
    "list": goods,
   }
  })

 # def get(self,request,Goods_name):
 #  goods = Goods.objects.filter(Goods_name=Goods_name).values()
 #  return Response({
 #   "code": 200,
 #   "message": "success",
 #   "data": {
 #    "list": goods,
 #   }
 #  })



 # def get(self, request,user_id,Goods_name):
 #  goods = Goods.objects.filter(
 #   Q(pk=user_id) or
 #   Q(Goods_name__icontains=Goods_name)
 # )
 #  return Response({
 #    "code": 200,
 #    "message": "success",
 #    "data": {
 #     "list": goods,
 #    }
 #   })