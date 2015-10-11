class MyIterator(object):
    def __int__(self,step):
        self.step = step

    def next(self):
        """Returns the next element."""
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """Returns the iterator itself."""
        return self

for el in MyIterator(range(4)):
    print el
