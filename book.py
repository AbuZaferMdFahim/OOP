class Book:
    def __init__(self,name,author):

        #assign to self object
        self.name = name
        self.author = author
        self.price = 0

    def set_Price(self,price):
        self.price = price

    def get_Price(self):
        return self.price

    def details(self):
        print("Book Name: ", self.name,"\nAuthor: ", self.author, "\nPrice: ", self.price, " Taka")






