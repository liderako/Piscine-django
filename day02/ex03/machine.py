import random
from beverages import HotBeverage
from beverages import Tea

class CoffeeMachine:
    def __init__(self):
        self.count = 0

    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90
        def     description(self):
            return ("An empty cup?! Gimme my money back!")
    
    class BrokenMachineException(Exception):
        def __init__(self):
            self.message = "This coffee machine has to be repaired."
            super(CoffeeMachine.BrokenMachineException, self).__init__(self.message) 


    def     repair(self):
        self.count = 0
        print ("Repair Coffee machine")

    def     serve(self, hotBeverage):
        n = random.randint(1, 100)
        self.count += 1
        if (self.count == 10):
            raise coffeeMachine.BrokenMachineException()
        if (n % 2 != 0):
            return (hotBeverage)
        else:
            return (CoffeeMachine.EmptyCup())

def     testMain():
    coffeeMachine = CoffeeMachine()
    try:
        raise coffeeMachine.BrokenMachineException()
    except Exception as e:
        print ("This coffee machine has to be repaired.")
        coffeeMachine.repair()

    print (coffeeMachine.serve(HotBeverage()))
    i = 0
    while (i < 10):
        try:
            print (coffeeMachine.serve(Tea()))
        except:
            coffeeMachine.repair()
        i += 1
if __name__ == '__main__':
    testMain()