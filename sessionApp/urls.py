from django.urls import path  
from .views import home,products,load_products

urlpatterns = [

	path('', home, name='home'),
	path('products/<int:pk>/', products, name='products'),
	path('load/', load_products, name='load_products'),

]