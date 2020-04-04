#hashing function to search a number in slot

class HashTable():
    #initialize slot and value if table
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size

    #put element in slot
    def put(self,key):
        hashValue=key%self.size
        if self.slots[hashValue]==None:
            self.slots[hashValue]=key
        else:
            if self.slots[hashValue]==key:
                self.slots[hashValue]=key
            else:
                nextSlot=(hashValue+1)%self.size
                while self.slots[nextSlot]!=None and self.slots[nextSlot]!=key:
                    nextSlot=(nextSlot)%self.size

                if self.slots[nextSlot] == None:
                    self.slots[nextSlot]=key
                else:
                    self.slots[nextSlot] = key


    def setItem(self,key):
        self.put(key)

h=HashTable()
h.setItem(44)
h.setItem(77)
h.setItem(89)
print(h.slots)