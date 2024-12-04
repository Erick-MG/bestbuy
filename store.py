from product import Product

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if product not in self.products:
            self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def buy_product(self, product_name: str, quantity: int):
        for product in self.products:
            if product.name == product_name:
                return product.buy(quantity)
        raise ValueError("Product not found.")