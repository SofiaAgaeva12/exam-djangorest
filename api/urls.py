from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from api.views import RegisterView, ProductsView, OrdersView, UserView, LastProductsView

urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', obtain_auth_token),
    path('register/', RegisterView.as_view(), name="register"),
    path('products/', ProductsView.as_view({'get': 'list', 'post': 'create', }), name="products"),
    path('last-products/', LastProductsView.as_view({'get': 'list', }), name="last-products"),
    path('products/<int:pk>', ProductsView.as_view({'get': 'retrieve', }), name="product-detail"),
    path('orders/', OrdersView.as_view({'get': 'list', 'post': 'create', }), name="orders"),
    path('orders/<int:pk>', OrdersView.as_view({'get': 'retrieve', }), name="order-detail"),
    path('user/<int:pk>', UserView.as_view(), name="profile"),
]
