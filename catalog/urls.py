from django.urls import path
from .views import ProductListView, ProductDetailView,category_list
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.product_list_by_category, name='product_list_by_category'),

]
