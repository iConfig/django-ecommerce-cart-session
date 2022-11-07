from django.shortcuts import render

import requests
from .models import Product 

# Create your views here

def home(request):
	products = Product.objects.all()
	return render(request, 'home.html', {'products':products})


def products(request, pk):
	product = Product.objects.get(pk=pk)
	recently_viewed_products = None

	if 'recently_viewed' in request.session:
		if pk in request.session['recently_viewed']:
			request.session['recently_viewed'].remove(pk)


		recently_viewed_products = Product.objects.filter(pk__in=request.session['recently_viewed'])
		request.session['recently_viewed'].insert(0, pk)
		if len(request.session['recently_viewed']) > 5:
			request.session['recently_viewed'].pop()
	else:
		request.session['recently_viewed'] = [pk]

	request.session.modified = True

	return render(request, 'products.html', {'product':product,'recently_viewed_products':recently_viewed_products})

def load_products(request):
	load = requests.get('https://fakestoreapi.com/products')
	for item in load.json():
		product = Product(
			title = item['title'],
			price = item['price'],
			description = item['description'],
			image_url = item['image']
			)
		product.save()


	return render(request, 'home.html')