from rest_framework import serializers

from user.models import Users


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields='__all__'