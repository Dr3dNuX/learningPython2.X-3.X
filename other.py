class name:
    data = 'spam'

    def __init__(self, value):
        self.data = value

    def printNames(self):
        print(self.data, name.data)    


class name2(name):
    def __init__(self):
        name.__init__(self, 2)

one = name(1)
two = name2()



one.printNames()
two.printNames()
