import beverages
import random

class CoffeeMachine:

    def __init__(self):
        self.bev_counter = 0

    # ok
    class EmptyCup(beverages.HotBeverage):
        def __init__(self,name="empty cup", price=0.9, description = "An empty cup?! Gimme my money back!"):
        	self.name = name
        	self.price = price
        	self.description = description
    
    class BrokenMachineException(Exception):
        def __init__(self,text= "This coffee machine has to be repaired."):
            Exception.__init__(self,text)

    def repair(self):
        self.bev_counter = 0
        print("The machine is repaired")

    def serve(self,my_beverage):
        self.my_beverage = my_beverage
        self.bev_counter += 1
        print("\nHot beverage served number :", self.bev_counter)
        if self.bev_counter == 10:
            raise self.BrokenMachineException
        # gestion de la boisson servie
        # une fois sur deux gobelet vide/boisson demandee
        bev_served = "EmptyCup"
        if random.randint(0, 1) == 0:
            bev_served = self.my_beverage
        # une fois sur deux la boissom appele/ empty
        return(bev_served)
       
if __name__ == '__main__':
    try:
        instance_CoffeMachine = CoffeeMachine()
        print(instance_CoffeMachine.serve(beverages.Coffee()))
        print(instance_CoffeMachine.serve(beverages.Tea()))
        print(instance_CoffeMachine.serve(beverages.Chocolate()))
        print(instance_CoffeMachine.serve(beverages.HotBeverage()))
        print(instance_CoffeMachine.serve(beverages.Coffee()))
        print(instance_CoffeMachine.serve(beverages.Chocolate()))
        print(instance_CoffeMachine.serve(beverages.HotBeverage()))
        print(instance_CoffeMachine.serve(beverages.HotBeverage()))
        print(instance_CoffeMachine.serve(beverages.Coffee()))
        print(instance_CoffeMachine.serve(beverages.HotBeverage()))
        print(instance_CoffeMachine.serve(beverages.Coffee()))
        print(instance_CoffeMachine.serve(beverages.Chocolate()))
        print(instance_CoffeMachine.serve(beverages.HotBeverage()))
        print(instance_CoffeMachine.serve(beverages.HotBeverage()))
        print(instance_CoffeMachine.serve(beverages.Coffee()))
        print(instance_CoffeMachine.serve(beverages.Chocolate()))
    except instance_CoffeMachine.BrokenMachineException as e:
        print(e)
        instance_CoffeMachine.repair()
