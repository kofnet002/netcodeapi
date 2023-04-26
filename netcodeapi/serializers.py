from rest_framework import serializers
from .models import Code, User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = "__all__"