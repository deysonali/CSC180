from hashlib import *

class seeker():

    

    def __init__(self):
        self.store = []
        for i in range (0,30000):
            (self.store).append(0)
    def add(self, name, price, qty, date):
        entry = [name, price, qty, date]
        hashval = hashlib.sha1(name).hexdigest()
        index = int(str(hashval), 16) % 1000
        #collision resolution
        if self.store[index] != 0:
            if hashlib.sha1(str(self.store[index][0])).hexdigest() == hashval:
                self.store[index][2] += 1
        else:
            if self.store[index] != 0:
                self.colresolve(name, price, qty, date, index)
                return     
            else:
                self.store[index] = entry
        return 
    #search when if doesn't exist
    def search(self, name):
        hashval = hashlib.sha1(name).hexdigest()
        index = int(str(hashval), 16) % 1000
        if self.store[index] == 0:
            negisbad = self.find(name,index)
            if negisbad == 0:
                return 0
        if hashlib.sha1(str(self.store[index][0])).hexdigest() == hashval:
            print name + "\n" + "Price: " + str(self.store[index][1]) + "\n" + "Quantity: " + str(self.store[index][2]) + "\n" + "Date: " + str(self.store[index][3])
            return    
        if hashlib.sha1(str(self.store[index][0])).hexdigest() != hashval:
            negisstillbad = self.find(name,index) 
            if negisstillbad == 0:
                return 0
        print "Not found"
        return 0
    def sold(self, name):
        hashval = hashlib.sha1(name).hexdigest()    
        index = int(str(hashval), 16) % 1000 
        if hashlib.sha1(str(self.store[index][0])).hexdigest() == hashval:
            if self.store[index][2] == 1:
                self.store[index] = 0
            else:
                self.store[index][2] -= 1    
        return 0
    def colresolve(self, name, price, qty, date, index):
        found = 0
        for i in self.store:
            if i == 0:
                found = 1
        if found != 0:
            (self.store).append(0,0,0,0,0,0,0,0,0,0)
        for i in range (1,11):
            if hashlib.sha1(str(self.store[index+i][0])).hexdigest() == hashlib.sha1('name'):
                self.store[index+i][2] += 1
                return 0 
            if hashlib.sha1(str(self.store[index+i][0])).hexdigest() == 0:
                self.store[index+i] =  [name, price, qty, date]
                return 0
        for i in range (0, len(self.store)):
            if hashlib.sha1(str(self.store[index+i][0])).hexdigest() == hashlib.sha1('name'):
                self.store[index+i][2] += 1
                return 0
            if hashlib.sha1(str(self.store[index+i][0])).hexdigest() == 0:
                self.store[index+i] = [name, price, qty, date]
                return 0
        #see if can place in next 10
        #for each one see if it should be added if same or empty
        #then heard place
        return 0
    def find(self, name, index):
        foundit = -1
        hashval = hashlib.sha1(name).hexdigest()
        for i in range (1,11):
            if hashlib.sha1(str(self.store[index+i][0])).hexdigest() == hashval:
                foundit = index+i
                break
        if foundit == -1:
            for i in range (0,len(self.store)):
                if hashlib.sha1(str(self.store[index+i][0])).hexdigest() == hashval:
                    foundit = index+i
                    break 
        index = foundit
        if foundit == -1:
            return -1
        else:
            print Name + "\n" + "Price: " + str(self.store[index][1]) + "\n" + "Quantity: " + str(self.store[index][2]) + "\n" + "Date: " + str(self.store[index][3])
        #search the next 10
        #then hard search
        return 0
#hash_object = hashlib.sha1('Hello World')
#hex_dig = hash_object.hexdigest()
#print(hex_dig) 
#print int(hex_dig,16)
#print int(hex_dig,16)+1

s = seeker()
print "ADD, SEARCH, SOLD, EXIT"
x = raw_input("")
while x != "Exit":
    if x == "Add":
        name = raw_input("Name: ")
        price = raw_input("Price: ")
        qty = int(raw_input("Quantity: "))
        date = raw_input("Date: ")
        s.add(name,price,qty,date)
        x = raw_input("ADD, SEARCH, SOLD, EXIT\n")
    if x == "Search":
        name = str(raw_input("Name: "))
        s.search(name)
        x = raw_input("ADD, SEARCH, SOLD, EXIT\n")
    if x == "Sold":
        name = raw_input("Name: ")
        s.sold(name)
        x = raw_input("ADD, SEARCH, SOLD, EXIT\n")
    if x == "Exit":
        break 

