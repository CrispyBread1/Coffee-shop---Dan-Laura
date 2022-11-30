class CoffeeShop:
    def __init__(self, name, till, list_of_drinks):
        self.shop_name = name
        self.till = till
        self.list_of_drinks = list_of_drinks

    
    def add_to_list_of_drinks(self, drink):
        self.list_of_drinks.append(drink)

    def take_money_from_customer(self, instance_of_customer):
        instance_of_customer.wallet -= self.list_of_drinks.price
        
    def add_money_to_till(self, drink):
        self.till += drink.price