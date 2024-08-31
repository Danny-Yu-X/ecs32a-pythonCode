class BossMachine:
    def __init__(self, price = 2.25, capacity = 500):
        self.numCans = 2
        self.capacity = capacity
        self.price = price
        self.cash = 0
        print("Adding a Boss Machine to the Empire")
    def set_price(self, price):
        if price > 0:
            self.price = price
    def get_cash_str(self):
        return "${:.2f}".format(self.cash)
    def buyBoss(self):
        if self.numCans > 0:
            print("Have a Boss")
            self.numCans = self.numCans - 1
            print("Number of cans reamining:", self.numCans)
            self.cash = self.cash + self.price
        else:
            print("Out of Coffee")
    def refillCans(self,numCans = 500):
        if self.numCans + numCans <= 500:
            self.numCans = self.numCans + numCans
            else:
                print("Can't add that many cans")
    def checkCans(self):
        return self.numCans

class SimBoss:
    def __init__(self):

        csmachine = BossMachine()
        engmachine = BossMachine()
        csmachine.buyBoss()
        csmachine.buyBoss()
        csmachine.buyBoss()
        csmachine.numCans = refillCans(100)
        engmachine.buyBoss()
        engmachine.buyBoss()
        engmachine.refillCans(500)
        print("CS machine has", csmachine.checkCans(), "cans.")
        print("ENG machine has", engmachine.checkCans(), "cans.")
        print("CS machine has", csmachine.get_cash_str))
        print("ENG amchine has", engmachine.get_cash_str())
        print("CS machine:", csmachine)
        if csmachine < engmachine:
            print("ENG machine wins!")
        else:
            print("CA machine wins!")

sim = SimBoss()
        
