
class Super:
    def superMethod(self):
        print('This method is from the super')
    
    def needProvider(self):
        self.provider()


class Sub(Super):
    def subMethod(self):
        print('This method is from the sub')
    
    def provider(self):
        print('nice')

x = Sub()

x.needProvider()