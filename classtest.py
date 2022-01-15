class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    
    def __repr__(self):
        return '{}'.format(self.name)
    
    def __str__(self):
        return str(['{} => {}'.format(item, self.__dict__[item]) for item in self.__dict__.keys()])
            
        #return 'Name = {}, Job = {}, Pay = ${:,}'.format(self.name,self.job,self.pay)
    

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
    


bob = Person('bob','DevOps',100000)
kriss = Manager('kriss', 'tech-lead', 200000)

kriss.giveRaise(.10)

print(kriss)