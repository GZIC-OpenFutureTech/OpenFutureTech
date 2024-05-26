"""
Person Class.py
author:张辰旭
date:2023.5.9
description:Person Class
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getFriends(self):
        return self.friends
    
    def getFriendsNames(self):
        return sorted([f.getName() for f in self.friends])
    
    def addFriend(self, person):
        if person not in self.friends:
            self.friends.append(person)
            person.addFriend(self)
    
    def addFriends(self, people):
        for person in people.getFriends():
            self.addFriend(person)

def testPersonClass():
    print('Testing Person Class...', end='')
    fred = Person('fred', 32)
    assert(isinstance(fred, Person))
    assert(fred.getName() == 'fred')
    assert(fred.getAge() == 32)
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

testPersonClass()