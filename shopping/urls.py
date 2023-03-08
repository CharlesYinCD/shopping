"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from goods import views as goods_view
from car import  views as cars_view
from order import views as orders_view
from user import views as users_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/goods',goods_view.GoodsView.as_view()),
    path('api/goods/<int:goods_id>',goods_view.GoodsDetailView.as_view()),
    # path('api/goods/<Goods_name>',goods_view.GoodsDetailView.as_view()),
    path('api/cars/<int:car_id>/',cars_view.ShoppingCars.as_view()),
    path('api/cars/',cars_view.AddShoppingCars.as_view()),
    path('api/orders/',orders_view.OrderView.as_view()),
    path('api/orders/<int:order_id>/',orders_view.OrderDetailView.as_view()),
    path('api/register',users_view.RegisterView.as_view()),
    path('api/login',users_view.LoginView.as_view()),
    path('api/users/<int:user_id>/',users_view.UpdatePasswordView.as_view())
]
