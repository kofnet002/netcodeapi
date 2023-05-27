from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from .serializers import CodeSerializer, UserSerializer
from .models import Code, User
from django.db.models import Q

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# from django.contrib.auth.models import User

# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['id'] = user.id
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class EndPoints(APIView):
    def get(self, request):
        endpoints = [
            "register/",
            "login/",
            "codes/",
            "codes/<id>/",
        ]
        return Response(endpoints)


class RegisterView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class GetCodes(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        user = request.user
        codes = user.code_set.all()
        search_param = request.query_params.get('search')

        if search_param:
            codes = codes.filter(
                Q(topic__icontains=search_param) |
                Q(code__icontains=search_param) |
                Q(url__icontains=search_param) |
                Q(author__icontains=search_param),
            )

        serializer = CodeSerializer(codes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'note': request.data,
            'image': request.FILES.get('code_image'),
        }
        _data = CodeSerializer(data=data),
        if _data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class CodeDetail(APIView):
    permission_classes = [IsAuthenticated,]

    def get_object(self, id):
        try:
            return Code.objects.get(id=id)
        except Code.DoesNotExist:
            raise Response("Object not found")

    def get(self, request, id):
        code = self.get_object(id)
        serializer = CodeSerializer(code)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        code = self.get_object(id)
        serializer = CodeSerializer(code, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        code = self.get_object(id)
        code.delete()
        return Response({"message": "Deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
