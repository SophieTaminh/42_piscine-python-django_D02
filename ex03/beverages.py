class HotBeverage:

    def __init__(self,name="hot beverage",price=0.3 ,description="Just some hot water in a cup."):
        self.price = price
        self.name = name
        self.description = description

    #retourne une description de l'instance
    def description(description):
        return(description)

    def __str__(self):
        return("name : {}\nprice : {:03.2f}\ndescription : {description}".\
       	format( self.name, self.price, description=HotBeverage.description(self.description)))

class Coffee(HotBeverage):
    def __init__(self,name="coffee",price=0.4,description="A coffee, to stay awake."):
        super().__init__(name,price,description) # appeler la class init de la classe parente
        
class Tea(HotBeverage):
    def __init__(self,name="tea"):
        super().__init__(name) # appeler la class init de la classe parente

class Chocolate(HotBeverage):
    def __init__(self,name="chocolate", price=0.5, description = "Chocolate, sweet chocolate..."):
        super().__init__(name,price,description) # appeler la class init de la classe parente

class Cappuccino(HotBeverage):
    def __init__(self,name="cappucino", price=0.45, description = "Un po’ di Italia nella sua tazza!"):
        super().__init__(name,price,description) # appeler la class init de la classe parente

#--------------------------------
if __name__ == '__main__':
    print("le hot_baverage parent") 
    Hot_Beverage = HotBeverage()
    print(Hot_Beverage)

    #le cafe
    print("\nCoffee") 
    Coffee_dev = Coffee()
    print(Coffee_dev)
    
    #le the
    print("\nTea") 
    Tea_dev = Tea()
    print(Tea_dev)

    #le chocolat
    print("\nChocolate") 
    Chocolate_dev = Chocolate()
    print(Chocolate_dev)

    #le cappuccino
    print("\nCappuccino") 
    Cappuccino_dev = Cappuccino()
    print(Cappuccino_dev)
