import collections

#Если использовать встроенные функции Python:

class FIFO_1:
    def __init__(self, lenght):
        self._collection = collections.deque(maxlen= lenght)
    def put(self,item):
        self._collection.append(item)
    def getCollection(self):
        return self._collection
    def print(self):
        print(self._collection)

class FIFO_2:
    _collection = []
    def __init__(self, lenght):
        self._collectionLenght = lenght
    def put(self,item):
        if(len(self._collection) == self._collectionLenght):
            self._collection.pop(0)
        self._collection.append(item)
    def getCollection(self):
        return self._collection
    def print(self):
        print(self._collection)