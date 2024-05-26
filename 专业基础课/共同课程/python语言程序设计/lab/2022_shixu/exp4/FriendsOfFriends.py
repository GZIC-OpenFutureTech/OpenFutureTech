"""
FriendsOfFriends.py
author:张辰旭
date:2023.04.11
description:find the friend of friend using dictionary
"""
def FriendsOfFriends(d):
    FOF = {}
    for name in d:
        friend = d[name]
        FOF[name] = set()
        for fof in friend:
            FOF[name].update(d[fof])
            FOF[name]=FOF[name]-friend
            FOF[name].discard(name)
    return FOF

d = {}
d["jon"] = set(["arya", "tyrion"])
d["tyrion"] = set(["jon", "jaime", "pod"])
d["arya"] = set(["jon"])
d["jaime"] = set(["tyrion", "brienne"])
d["brienne"] = set(["jaime", "pod"])
d["pod"] = set(["tyrion", "brienne", "jaime"])
d["ramsay"] = set()
print(FriendsOfFriends(d))