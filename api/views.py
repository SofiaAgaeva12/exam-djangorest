from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import MyUser, Product, Order
from api.serializers import RegisterSerializer, ProductSerializer, OrderSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = MyUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": 'Пользователь создан', "status:": status.HTTP_201_CREATED},
                        status=status.HTTP_201_CREATED, headers=headers)


class ProductsView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    model = Product
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class LastProductsView(viewsets.ModelViewSet):
    queryset = Product.objects.all() if len(Product.objects.all()) < 5 else Product.objects.all()[
                                                                            len(Product.objects.all()) - 5:len(
                                                                                Product.objects.all())]
    model = Product
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class OrdersView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    model = Order
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id']


class UserView(APIView):
    def get(self, request, pk):
        user = MyUser.objects.filter(id=pk).get()
        order = Order.objects.filter(user=pk).all()
        serializer1 = UserSerializer(user)
        serializer2 = OrderSerializer(order, many=True)
        return Response({"user": serializer1.data, "order": serializer2.data})
