class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = list(reversed(nestedList))

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.stack.extend(reversed(top.getList()))
        return False