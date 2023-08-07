from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.

def home(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Топ товаров'
    }

    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'catalog/contacts.html')


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории'
    }

    return render(request, 'catalog/categories.html', context)


def category_product(request, pk):
    category_item = Category.objects.get(id=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': category_item.name
    }
    return render(request, 'catalog/category_product.html', context)