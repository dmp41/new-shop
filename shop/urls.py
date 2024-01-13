from django.urls import path
from . import views

app_name = 'shop'   # app name

# pattern for the index page, all products and each product
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:product_slug>/', views.product_detail, name='product'),
]