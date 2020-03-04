from hashtable import HashTable

class Set:

    def __init__(self, elements=None):
        self.hashtable = HashTable()
        self.size = self.hashtable.size

    def contains(self, element):
        return self.hashtable.contains(element)
    
    def add(self, element):
        if self.contains(element): 
            raise ValueError 
        else:
            return self.hashtable.set(element, 3)
    
    def remove(self, element):
        if self.contains(element):
            self.hashtable.delete(element)
        else:
            return KeyError
    
    def union(self, other_set):
        new_set = Set()
        for key in self.hashtable.keys():
            new_set.add(key)
        for key in other_set.hashtable.keys():
            new_set.add(key)
        return new_set
        
    def difference(self, other_set):
        new_set = Set()
        for key in other_set.hashtable.keys():
            if not self.hashtable.contains(key):
                new_set.add(key)
        return new_set
    
    def is_subset(self, other_set):
        for key in other_set.hashtable.keys():
            if not self.hashtable.contains(key):
                return False
        return True




            


    
    

