from rest_framework import serializers

from car.models import Cars


class ShoppingCarSerializers(serializers.ModelSerializer):
    class Meta:
        model=Cars
        fields = '__all__'
