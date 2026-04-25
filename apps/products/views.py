from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q
def product_list(request):
    products = Product.objects.all()

    query = request.GET.get('q')
    category_id = request.GET.get('category')

    # 🔍 ПОИСК
    if query:
        query = query.strip()  # Убираем лишние пробелы
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    # 📂 ФИЛЬТР ПО КАТЕГОРИИ
    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, 'products/product_list.html', {
        'products': products,
        'selected_category': int(category_id) if category_id and category_id.isdigit() else None
    })

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})



