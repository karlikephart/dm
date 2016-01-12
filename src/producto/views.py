from django.shortcuts import render

from .models import Producto

# Create your views here.


def detail_view(request):
	#un producto
	if request.user.is_authenticated():

		producto = Producto.objects.all().first()
		template = "detail_view.html"
		context = {
			"title": "HOLA DETAIL",
			"objeto": producto
		}

	else:
		template = "not_found.html"
		context = {}

	return render(request, template, context)


def list_view(request):
	#todos los productos
	print request
	queryset = Producto.objects.all()
	template = "list_view.html"
	context = {
		"queryset": queryset
	}
	return render(request, template, context)