from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('create_product/', views.create_product, name="create_product"),
    path('update_product/<int:pk>/', views.update_product, name="update_product"),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
]
