from os import truncate
import time
import threading

# they can get sick and other random events have a list that randomly picks one thing
# like they died or got sick lost a leg
# also they age and afer they get to a certn age they die

class hopper:
    def __init__(self) -> None:
        self.name = ''
        self.color = ''
        self.belly = []

    def bellyFunc(self,operation,food=None):
        
        if operation == 'feed':
            self.belly.append(food)
        elif operation == 'returnFood':
            return self.belly
        
    def hunger(self):
        print("hunger started")
        while True:
            if self.belly:
                time.sleep(10)
                self.belly.pop()
                print('ive lost an item')
            else:
                time.sleep(10)
                print('please feed me')
            
        # ether fill the belly or return whats in it
        # also have a timer to say when hes full or needs to eat

class handler:
    def __init__(self) -> None:
        self.invantory = {}
        self.money = 0
        self.name = 'Name'
        self.foodlist = []
    
    def gameloop(self):
        while True:
            user_input = input('>> ')
            if user_input == 'shop':
                
                    

                    

    
    
    # the handler class have the inventory of the handler
    # let you buy cages and items
    # allows you to have food and money
    # hanles input for the main ui to interface with the hoppers
    # invantory showing fuctions
    # money
    # maybe even have a save file sytem using opbject pickeling

class shop:
    
    # items can be stored in a key value nested dic with price so pizza : 20
    def __init__(self) -> None:
        """
        self.items = {
            'food' : ['pizza','chip','hamberger'],
            'health' : ['flu shot', 'antibiotix','leg sergery']
        }
        """
        self.items = ['pizza', 'flesh', 'brains']

    def listItems(self):
        return self.items

    def saleItem(self, handlerOb, item):
        if item in self.items:
            print('you have picked this item {}'.format(item))
            print('i will give it to you')
            handlerOb.foodlist.append(item)
            self.items.pop(item)
            handlerOb.money -= 10
    

    # the shop class
    # have items and teir lists
    # have items randomly restock
    # have sales for items like food litter and medicin and cages
    pass
theshop = shop()
guy = handler()
h1 = hopper()
h1.name = 'jerry'
h1.color = 'red'




h1.bellyFunc('feed','jeans')
h1.bellyFunc('feed','Carrot')


        


t1 = threading.Thread(target=h1.hunger)
t2 = threading.Thread(target=guy.gameloop)

print('starting one')
t1.start()
print('starting two')
t2.start()