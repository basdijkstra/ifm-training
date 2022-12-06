class Webshop:

    def __init__(self):
        self.payment_provider = Stripe()
        self.order_list = []
        self.manager = Employee('Susan', 'Jones')

    def place_order(self, article, amount):
        self.order_list.append(Order(article, amount))

    def checkout_order(self, order):
        self.payment_provider.pay(order.price)


class Stripe:

    def __init__(self):
        pass

    def pay(self, price):
        pass


class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Order:

    def __init__(self, article, amount):
        self.article = article
        self.amount = amount
