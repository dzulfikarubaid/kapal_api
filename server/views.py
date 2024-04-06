from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'detail':'nomor pegawai atau password salah'}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token':token.key, 'user':serializer.data})

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if password != confirm_password:
            return Response({"error": "Password and confirm password do not match."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def test(request):
    return Response({'message': 'Hello, world!'})

@api_view(['POST'])
def logout(request):
    return Response({'message': 'Hello, world!'})