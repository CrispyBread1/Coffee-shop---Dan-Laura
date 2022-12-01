import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.drinks = Drink("Americano", 4)
        self.instance_of_coffee_shop = CoffeeShop("boy'z Beanz" , 100)
        self.instance_of_customer = Customer("Brianne", 18, 500)
        # self.instance_of_drink = Drink()

    def test_has_nameI(self):
        self.assertEqual("boy'z Beanz", self.instance_of_coffee_shop.shop_name)

    def test_coffe_shop_has_drinkz(self):
        self.instance_of_coffee_shop.add_to_list_of_drinks(self.drinks)
        self.assertEqual(1, len(self.instance_of_coffee_shop.list_of_drinks))

    def test_customer_has_name_and_money(self):
        self.assertEqual("Brianne", self.instance_of_customer.customer_name)
        self.assertEqual(500, self.instance_of_customer.wallet)

    # def test_coffee_shop_has_drinks(self):
    #     drink_1 = Drink("Americano", 4)
    #     drink_2 = Drink("Tea", 5)
    #     self.instance_of_coffee_shop.add_to_list_of_drinks(drink_1)
    #     self.instance_of_coffee_shop.add_to_list_of_drinks(drink_2)
    #     self.assertEqual(2, len(self.instance_of_coffee_shop.list_of_drinks))

    def test_customer_buys_drink(self):
        # drink_1 = Drink("Americano", 4)
        # self.instance_of_coffee_shop.add_to_list_of_drinks(drink_1)
        self.instance_of_customer.give_money_to_coffeeshop(self.drinks)
        self.instance_of_coffee_shop.add_money_to_till(self.drinks)
        self.assertEqual(496, self.instance_of_customer.wallet)
        self.assertEqual(104, self.instance_of_coffee_shop.till)

    def test_customer_is_old_enough_to_drink(self):
        self.instance_of_coffee_shop.check_age_of_customer(self.instance_of_customer)
        self.assertEqual(True, bool(self.instance_of_coffee_shop.check_age_of_customer))

    def test_customer_buys_drink(self):
        self.instance_of_coffee_shop.sell_to_customer(self.instance_of_customer, self.drinks)
        # self.assertEqual(496, self.instance_of_customer.wallet)
        self.assertEqual(104, self.instance_of_coffee_shop.till)
