from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from django.contrib import messages
from .cart import Cart
Product = apps.get_model('products', 'Product')

def cart_view(request):
    cart = Cart(request)
    items, total_price = cart.get_items(Product)


    return render(request, 'cart/cart.html', {
        'items': items,
        'total_price': total_price
    })


def add_to_cart(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)

    cart.add(product.id)

    messages.success(request, "Товар добавлен в корзину 🛒")

    return redirect('product_detail', id=id)


def remove_from_cart(request, id):
    cart = Cart(request)
    cart.remove(id)

    return redirect('cart')


def update_cart(request, id):
    if request.method == 'POST':
        quantity = max(1, int(request.POST.get('quantity', 1)))


        cart = Cart(request)
        cart.update(id, quantity)

    return redirect('cart')

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')