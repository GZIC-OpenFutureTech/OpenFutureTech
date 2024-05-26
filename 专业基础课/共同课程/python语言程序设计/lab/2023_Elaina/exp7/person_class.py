"""
person_class.py
author: Elaina
date: 2023/12/14
description: Create a class with some functions.
"""

class Person:
    Person = []

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.friends = []
        Person:Person.append(self)

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getFriends(self):
        return self.friends

    def getFriendsNames(self):
        names = []
        for person in self.friends:
            names.append(person.name)
        names.sort()
        return names

    def addFriend(self, person):
        if person not in self.friends:
            self.friends.append(person)
            person.friends.append(self)
            return True
        else:
            print(f'{person.name} is already a friend of {self.name}')
            return False

    def addFriends(self, person):
        for p in person.friends:
            if p not in self.friends and p != self and p != person:
                self.friends.append(p)

    def print(self):
        print(self.name, self.age)
        for p in self.friends:
            print(p.name)

def testPersonClass():
    print('Testing Person Class...', end='')
    fred = Person('fred', 32)
    assert(isinstance(fred, Person))
    assert(fred.getName() == 'fred')
    assert(fred.getAge() == 32)
    # Note: person.getFriends() returns a list of Person objects who
    # are the friends of this person, listed in the order that
    # they were added.
    # Note: person.getFriendNames() returns a list of strings, the
    # names of the friends of this person. This list is sorted!
    assert(fred.getFriends() == [ ])
    assert(fred.getFriendsNames() == [ ])
    wilma = Person('wilma', 35)
    assert(wilma.getName() == 'wilma')
    assert(wilma.getAge() == 35)
    assert(wilma.getFriends() == [ ])
    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred])
    assert(wilma.getFriendsNames() == ['fred'])
    assert(fred.getFriends() == [wilma]) # friends are mutual!
    assert(fred.getFriendsNames() == ['wilma'])
    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred]) # don't add twice!
    betty = Person('betty', 29)
    fred.addFriend(betty)
    assert(fred.getFriendsNames() == ['betty', 'wilma'])
    pebbles = Person('pebbles', 4)
    betty.addFriend(pebbles)
    assert(betty.getFriendsNames() == ['fred', 'pebbles'])
    barney = Person('barney', 28)
    barney.addFriend(pebbles)
    barney.addFriend(betty)
    barney.addFriends(fred) # add ALL of Fred's friends as Barney's friends
    assert(barney.getFriends() == [pebbles, betty, wilma])
    assert(barney.getFriendsNames() == ['betty', 'pebbles', 'wilma'])
    fred.addFriend(wilma)
    fred.addFriend(barney)
    assert(fred.getFriends() == [wilma, betty, barney])
    assert(fred.getFriendsNames() == ['barney', 'betty', 'wilma']) # sorted!
    assert(barney.getFriends() == [pebbles, betty, wilma, fred])
    assert(barney.getFriendsNames() == ['betty', 'fred', 'pebbles', 'wilma'])
    print('Passed!')

if __name__ == "__main__":
    testPersonClass()
