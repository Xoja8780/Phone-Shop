class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id] += 1
        else:
            self.cart[product_id] = 1
        self.save()

    def update(self, product_id, quantity):
        product_id = str(product_id)

        if quantity > 0:
            self.cart[product_id] = quantity
        else:
            self.remove(product_id)

        self.save()

    def remove(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        if 'cart' in self.session:
            del self.session['cart']
            self.save()

    def save(self):
        self.session.modified = True

    def get_items(self, Product):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        items = []
        total_price = 0

        # создаём set существующих id
        existing_ids = set(str(p.id) for p in products)

        # 🧹 удаляем несуществующие товары из корзины
        for product_id in list(self.cart.keys()):
            if product_id not in existing_ids:
                del self.cart[product_id]

        for product in products:
            quantity = self.cart[str(product.id)]
            subtotal = product.price * quantity
            total_price += subtotal

            items.append(
                {
                    'product': product,
                    'quantity': quantity,
                    'subtotal': subtotal
                }
            )
        self.save()  # сохраняем изменения после очистки несуществующих товаров

        return items, total_price

    def get_total_quantity(self):
        return sum(self.cart.values())
