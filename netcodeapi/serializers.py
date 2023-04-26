from rest_framework import serializers
from .models import Code, User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
    
    # OVERWRITE CREATE METHOD TO HASH USER PASSWORD
    def create(self, validated_data):
        password = validated_data.pop("password", None) # extract password
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = "__all__"