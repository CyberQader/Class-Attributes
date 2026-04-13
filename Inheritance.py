class Food:
    def __init__(self,name,price):
        self.name = name
        self.name = price

        print(f'{self.name} Food Is Created From Main Class')

    def eat(self):
        print(f'Eat Method From Base Class')

class Apple (Food):
    def __init__(self,name,price,amount):

        super().__init__(name,price)

        self.amount = amount
        self.price = price

        print(f'{self.name} Is Created From Derived Class A Prive Is {self.price} A Mount Is {self.amount}')

    def get_from_tree(self):
        print(f'Get From Tree From Derived Class')

food_two = Apple('pizza',60,303)
food_two.eat()
food_two.get_from_tree()