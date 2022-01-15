class Indexer():

    def __init__(self, start, stop) -> None:
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        
        self.value += 1
        return self.value


for i in Indexer(1, 50):
    print(i)
