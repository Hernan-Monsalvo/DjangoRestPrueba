# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


@api_view(['GET'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)

        return Response(users_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        print(user_serializer)
        if user_serializer.is_valid():
            print(user_serializer)
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_register_view(request):
    if request.method == 'POST':
        user_serializer = RegisterSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def user_login_view(request):

    if request.method == 'GET':
        return Response({"message": "login"}, status=status.HTTP_200_OK)

    if request.method == 'POST':
        login_serialized = LoginSerializer(data=request.data)
        print("loginserialized: ", login_serialized)
        if login_serialized.is_valid():
            return Response({"message": "token"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "no valido", "errors": login_serialized.errors}, status=status.HTTP_400_BAD_REQUEST)
