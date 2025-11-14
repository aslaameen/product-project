from django.shortcuts import render, redirect

from product_app.forms import ProductForm
from product_app.models import Product


# Create your views here.
def product(request):
    data = ProductForm()
    if request.method == 'POST':
        data=ProductForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request, "add.html", {"data":data})


def view(request):
    data = Product.objects.all()
    return render(request, 'view.html', {'data':data})

def update(request,id):
    prod_up=Product.objects.get(id=id)
    if request.method == "POST":
        up_form=ProductForm(request.POST,instance=prod_up)
        if up_form.is_valid():
            up_form.save()
            return redirect('View')

    else:
        up_form=ProductForm(instance=prod_up)
    return render(request, 'update.html', {"data":up_form})


def delete(request,id):
    prod_del=Product.objects.get(id=id)
    prod_del.delete()
    return redirect('View')


# corona dashbord

def index(request):
    return render (request,'index.html')