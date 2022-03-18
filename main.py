class Item:
    pay_rate = 0.8  # the pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity  {quantity} is not greater or equal to zero"

        # Assign to sel object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.price}',{self.quantity})"





class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0 ):
        super().__init__(
            name, price, quantity
        )
        # Run validations to the received arguments
        assert broken_phones >= 0, f"broken_phones {broken_phones} is not greater or equal to zero"

        # Assign to sel object
        self.broken_phones = broken_phones

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.price}',{self.quantity})"



item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 5)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)
phone1 = Phone('jscPhoneV10', 500, 5, 0)

phone2 = Phone('jscPhoneV20', 700, 5, 0)
print(Item.all)
print(Phone.all)

