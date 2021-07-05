from django.db.models import Q
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    password2 = serializers.CharField(write_only=True)

    def validate_name(self, value):

        names = User.objects.all().values_list('name', flat=True)
        print(names)
        print(value)
        if value in names:
            raise serializers.ValidationError("Error, nombre ya existe")  # dispara error de validacion
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("password fields must match")
        return data

    def create(self, validated_data):
        del validated_data["password2"]
        return User.objects.create(**validated_data)



class LoginSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField()

    def validate(self, data):
        print("validate data: ", data)
        print(data['password'])
        queryset = User.objects.all()

        try:
            if data['name'] is not None:
                print("hay nombre")
            if data['email'] is not None:
                print("hay email")
        except:
            raise serializers.ValidationError("faltan campos")

        user = queryset.filter(name__icontains=data['name'])
        print(user[0].password, data['password'])
        if len(user) > 0:
            print("usuario encontrado: ", user[0].name, user[0].password, data["password"])

            if user[0].password == data["password"]:
                print("login OK")
            else:
                raise serializers.ValidationError("contraseña incorrecta")

        else:
            print('no encontrado')
            raise serializers.ValidationError("usuario no encontrado")

        return data
