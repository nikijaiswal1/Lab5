class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print("Title:", self.title, "| Author:", self.author, "| Price:", self.price)

    def update_price(self, new_price):
        self.price = new_price

book1 = Book("Python Programming", "Guido van Rossum", 1200)
book1.display_info()
book1.update_price(1500)
book1.display_info()
