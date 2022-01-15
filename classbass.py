from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    def method(self):
        print('in Super.method')
    
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass



class Provider(Super):
    def action(self):
        print('in provider')


x = Super()