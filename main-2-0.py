import time


class hopper:
    def __init__(self) -> None:
        self.name = ''
        self.color = ''
        self.belly = []

    def bellyFunc(self,operation,food=None):
        
        if operation == 'feed':
            self.belly.append(food)
            
        elif operation == 'showBelly':
            return self.belly
        


def killHooper(hop):
    print('{} has died'.format(hop.name))
    




h1 = hopper()
h1.name = 'Jake'
h1.color = 'red'
h1.belly = ['pizza','beer','chip']
h2 = hopper()

killHooper(h1)

print(h1.name)
print(h2)