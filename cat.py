class Cat:
    def __init__(self,color,action):
        self.color = color
        self.action = action

    def view(self,num,clr):
        num=  num+5
        self.clr = clr
        clr[0] = "green"
        print("Method inside: ", num)
        print("Method inside: ", clr)

colors = ["Black","Red", "Yellow", "Blue"]
c1 = Cat("White", "Jumping")
x= 55

c1.view(x,colors)
print("Method Outside: ", x)
print("Method Outide: ", colors)