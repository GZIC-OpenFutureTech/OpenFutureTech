"""
FriendsOfFriends.py
author: Elaina
date: 2023/11/14
description: get the friends of the person
"""

def FriendsOfFriends(d):
    ans = dict()
    for person in d:
        ans[person] = set()
    for person in d:
        for friends in d[person]:
            for friends_of_friends in d[friends]:
                if person != friends_of_friends and friends_of_friends not in d[person]:
                    ans[person].add(friends_of_friends)
    return ans
        
d = { }
d["jon"] = set(["arya", "tyrion"])
d["tyrion"] = set(["jon", "jaime", "pod"])
d["arya"] = set(["jon"])
d["jaime"] = set(["tyrion", "brienne"])
d["brienne"] = set(["jaime", "pod"])
d["pod"] = set(["tyrion", "brienne", "jaime"])
d["ramsay"] = set()

print(FriendsOfFriends(d))
