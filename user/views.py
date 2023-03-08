from django.shortcuts import render
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
# from django.contrib.auth.models import User
from .serializer import RegisterSerializers
import jwt
import datetime
from django.conf import settings
from extensions.auth import JWTQueryParamsAuthentication

class RegisterView(APIView):
    authentication_classes = []
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        password2 = request.data.get('password2')
        if Users.objects.filter(username=username):
            return Response({'msg': '该用户已注册！', 'code': 400})
        else:
            if password == password2:
                user_data = {'username': username, 'password': make_password(password)}
                user_serializer = RegisterSerializers(data=user_data)
                if user_serializer.is_valid():
                    user_serializer.save()
                    return Response({'msg': '注册成功！', 'code': 200})
                else:
                    return Response({'msg': user_serializer.errors, 'code': 400})
            else:
                return Response({'msg': '两次密码不一致！', 'code': 400})



class LoginView(APIView):
    authentication_classes = []
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = Users.objects.filter(username=username).first()
        if user and check_password(password, user.password):
            salt = settings.SECRET_KEY
            headers = {
                'typ':'jwt',
                'alg':'HS256'
            }
            payload={
                'user_id':user.id,
                'username':user.username,
                'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=5)
            }
            token = jwt.encode(payload=payload,key=salt,algorithm='HS256',headers=headers).decode('utf-8')
            return Response({'msg': '登录成功', 'code': 200, 'user_id': user.id,'token':token})
        else:
            return Response({'msg': '登录失败', 'code': 400})




class UpdatePasswordView(APIView):
    def put(self, request,user_id):
        oldPassword = request.data.get('oldPassword')
        newPassword = request.data.get('newPassword')
        user = Users.objects.filter(id=user_id).first()
        if not check_password(oldPassword,user.password):
            return Response({'message': '原密码输入有误'})
        user.password=make_password(newPassword)
        user.save()
        return Response({'message': '修改成功'})

