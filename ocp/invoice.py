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

class InvoicePrinter:

    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    def print_invoice(self):
        print(f'{self.invoice.quantity}x {self.invoice.book.title} - {self.invoice.book.author}')
        print(f'Discount: {self.invoice.discount}')
        print(f'Tax rate: {self.invoice.tax}')
        print(f'Total: ${self.invoice.total}')

class InvoicePersister:

    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    def save_to_file(self):
        # Do something to save the invoice to a file
        pass

    def save_to_database(self):
        # Do something to save the invoice to a database
        pass

    def save_to_cloud(self):
        # Do something to save the invoice to a SaaS system
        pass
