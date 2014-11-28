# POO exos 2
import sys

class Mapping:

    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable) # call __update and not the update() method of MappingSub

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of update() method --> _Mapping__update
    
class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)



