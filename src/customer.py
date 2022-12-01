class Customer:
    def __init__(self, name, age, wallet):
        self.customer_name = name 
        self.age = age
        self.wallet = wallet


    def give_money_to_coffeeshop(self, drink):
        self.wallet -= drink