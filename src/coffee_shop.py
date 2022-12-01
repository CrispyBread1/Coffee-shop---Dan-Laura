class CoffeeShop:
    def __init__(self, name, till):
        self.shop_name = name
        self.till = till
        self.list_of_drinks = []
        # self.eligibility_to_drink = check_age_of_customer

    
    def add_to_list_of_drinks(self, drink):
        self.list_of_drinks.append(drink)

    # def take_money_from_customer(self, instance_of_customer):
    #     instance_of_customer.wallet -= self.list_of_drinks.price
        
    def add_money_to_till(self, drink):
        self.till += drink

    def check_age_of_customer(self, customer):
        if customer.age <= 16:
            return False
        return True

    
    def sell_to_customer(self, customer, drink):
        can_serve_customer = self.check_age_of_customer(customer)
        if can_serve_customer == True:
            customer.give_money_to_coffeeshop(drink.price)
            self.add_money_to_till(drink.price)
        