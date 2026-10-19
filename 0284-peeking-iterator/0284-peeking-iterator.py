class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        return self._next

    def next(self):
        val = self._next
        self._next = self.iterator.next() if self.iterator.hasNext() else None
        return val

    def hasNext(self):
        return self._next is not None