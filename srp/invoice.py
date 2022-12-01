from srp.book import Book


class Invoice:

    def __init__(self, book: Book, quantity, discount, tax):
        self.book = book
        self.quantity = quantity
        self.discount = discount
        self.tax = tax
        self.total = self.calculate_total()

    def calculate_total(self):
        price_before_tax = (self.book.price - (self.book.price * self.discount)) * self.quantity
        price_after_tax = price_before_tax * (1 + self.tax)
        return price_after_tax

    def print_invoice(self):
        print(f'{self.quantity}x {self.book.title} - {self.book.author}')
        print(f'Discount: {self.discount}')
        print(f'Tax rate: {self.tax}')
        print(f'Total: ${self.total}')

    def save_invoice_to_file(self):
        # Perform some logic that stores invoice to a file
        pass
