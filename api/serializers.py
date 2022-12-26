from rest_framework import serializers

from api.models import MyUser, Product, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password', 'avatar']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password', 'avatar']

    def create(self, validated_data):
        user = MyUser.objects.create(username=validated_data['username'], email=validated_data['email'],
                                     avatar=validated_data['avatar'])
        user.set_password(validated_data['password'])
        user.save()
        return user
