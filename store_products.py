class Products:

    def __init__(self, products):
        self.name = products[0]['name']
        self.price = products[0]['price']
        self.category = products[0]['category']

    def update_price(self, percent_change, is_increased):
        if is_increased is True:
            self.price = self.price * (1 + percent_change)
            print(f"The price is now {self.price}")
        elif is_increased is False:
            self.price = self.price - (self.price * (1 + percent_change))
            print(f"The price is now {self.price}")

    def print_info(self):
        print(f"Product: {self.name}\n{self.price}\n{self.category}")


class Store:

    def __init__(self):
        self.name = ""
        self.price = ""
        self.category = ""

    def add_product(self):
        product_list = []
        product = {}
        yes_or_no = input('Would you like to add a product to our site?: ')
        if "yes" in yes_or_no:
            print("Let's get started then!")
            product['name'] = input("Enter Product Name: ")
            product['price'] = input("Enter Cost of Product: ")
            product['category'] = input("Enter the Category of the Product: ")
            product_list.append(product)
            return product_list
        else:
            print("No Problem! Come back and see me when you are ready")
            exit()

New_Product = Store()
Item_1 = New_Product.add_product()
print(Item_1)
Sword = Products(Item_1)
print(Sword)
