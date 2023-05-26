class Item:
    def __init__(self,name: str, price: float, quantity=0):
        #run validation to recieve arguments
        assert price >= 0, f"price {price} is not greater or equal zero"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal zero"

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotal(self):
        return self.price * self.quantity

item1 = Item("Phone",100,1)
item2 = Item("Tv",1000,2)

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item2.name)
print(item2.price)
print(item2.quantity)