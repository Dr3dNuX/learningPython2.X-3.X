

class Super():
    addr = "Hello World"
    
    def sayName(self, name):
        print('Hello {} nice to meet you'.format(name))
    
    def goodbyee(self):
        self.goodbye()

class Sub(Super):
    def sayName(self, name):
        print('Goodbye {} i will miss you'.format(name))
    
    def goodbye(self):
        print('goodbye')


class Number():
    def __init__(self,number) -> None:
        self.data = number

    def __sub__(self, otherNumber):
        return Number(self.data - otherNumber)
    
    def __repr__(self) -> str:
        return str(self.data)


y = Number(6)

print(y - 5)