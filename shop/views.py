from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.
def index(request):
    return render(request, 'index.html')
# Create your views here.

def product_detail(request, product_slug):
    product = get_object_or_404(Product, product_slug=product_slug) # get single data
    # в product помещаем все данные о текущем товаре. в дальнейшем в шаблоне будем вызывать так: product.title
    # где title - название одного из полей товара из созданной нами модели в models.py
    context = {
        'product' : product,
    }
    return render(request, 'card.html', context)

