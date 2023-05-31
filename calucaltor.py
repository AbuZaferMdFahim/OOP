class myCalculator:
    def product(self,*nums):
        product = 1
        for s in nums:
            product = product * s
        print(product)

cal = myCalculator()
cal.product(2,4)
cal.product(2,3,4,1)
cal.product((2))
