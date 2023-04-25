from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CodeSerializer
from .models import Code


# Create your views here.
class AllCodes(APIView):
    def get(self, request):
        codes = Code.objects.all()
        serializer = CodeSerializer(codes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = CodeSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

class CodeDetail(APIView):
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
        return Response(serializer.errors, status=status.HTTP_201_CREATED)
    
    def delete(self, request, id):
        code = self.get_object(id)
        code.delete()
        return Response({"message": "Deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)