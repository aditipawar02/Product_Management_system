from django.shortcuts import render
from PM_app.models import Product
from django.shortcuts import redirect


# Create your views here.

def index(request):
	return render(request , 'index.html')


def add_product(request):
	if request.method == 'POST':
		product_name = request.POST.get('product_name')
		product_price = request.POST.get('product_price')
		product_quantity = request.POST.get('product_quantity')
		product_category = request.POST.get('product_category')
		image=request.FILES.get("product_image")
		print(image)
		obj = Product(name = product_name , price = product_price , quantity = product_quantity , category = product_category ,image  =
		image)
		obj.save()
		return redirect("/list/")
	return render(request , 'add.html')

def list_product(request):
	data = Product.objects.all()
	print(data)
	return render(request , 'list.html' , context ={'data' : data})

def delete(request , id):
	obj = Product.objects.get(id=id)
	obj.delete()
	return redirect("/list/")

def update(request , id ):
	obj = Product.objects.get(id = id)
	if request.method == "POST" :
		obj.name = request.POST.get('product_name')
		obj.price = float(request.POST.get('product_price'))
		obj.quantity = int(request.POST.get('product_quantity'))
		obj.category = request.POST.get('product_category')
		obj.save()
		return redirect('/list/')
	return render(request , 'update.html' , context={'obj' : obj})


def list_product(request):
    data = Product.objects.all()

    for product in data:
        product.total_bill = product.price * product.quantity

    return render(request, 'list.html', {'data': data})