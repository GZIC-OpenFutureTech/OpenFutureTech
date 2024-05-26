"""
ContainsPythagoreanTriple.py
author:张辰旭
date:2023.04.11
description:Find the name with the most occurrences in the list, using three methods of different time complexity
"""
#O(n**2)
def MostCommonName_On2(L):
    max_count = 0
    most_common_names = set()
    for name in L:
        count = 0
        for other in L:
            if name == other:
                count += 1
        if count > max_count:
            max_count = count
            most_common_names = set([name])
        elif count == max_count:
            most_common_names.add(name)
    if len(most_common_names) == 0:
        return None
    elif len(most_common_names) == 1:
        return most_common_names.pop()
    else:
        return most_common_names

#O(nlogn)
def MostCommonName_Onln(L):
    if len(L)==0:
        return None
    name_count = {}
    for name in L:
        if name not in name_count:
            name_count[name] = 1
        else:
            name_count[name] += 1
    sorted_names = sorted(name_count.items(), key=lambda x: x[1], reverse=True)#这里sorted函数的时间复杂度是O(nlogn)
    max_count = sorted_names[0][1]
    most_common_names = set()
    for name, count in sorted_names:
        if count == max_count:
            most_common_names.add(name)
        else:
            break
    if len(most_common_names) == 0:
        return None
    elif len(most_common_names) == 1:
        return most_common_names.pop()
    else:
        return most_common_names

#O(n)
def MostCommonName_On(L):
    if len(L)==0:
        return None
    name_list = {}
    for name in L:
        if name not in name_list:
            name_list[name] = 1
        else:
            name_list[name] += 1
    max_count = max(name_list.values())
    most_common_names = set()
    for name, count in name_list.items():
        if count == max_count:
            most_common_names.add(name)
    if len(most_common_names) == 0:
        return None
    elif len(most_common_names) == 1:
        return most_common_names.pop()
    else:
        return most_common_names

print("O(n**2)")
print(MostCommonName_On2(["Jane", "Aaron", "Cindy", "Aaron"])== "Aaron")
print(MostCommonName_On2(["Jane", "Aaron", "Jane", "Cindy", "Aaron"])== {"Aaron", "Jane"})
print(MostCommonName_On2(["Cindy"]) == "Cindy")
print(MostCommonName_On2(["Jane", "Aaron", "Cindy"]) == {"Aaron","Cindy", "Jane"})
print(MostCommonName_On2([]) == None)
print("#==============================================================================")

print("O(nlogn)")
print(MostCommonName_Onln(["Jane", "Aaron", "Cindy", "Aaron"])== "Aaron")
print(MostCommonName_Onln(["Jane", "Aaron", "Jane", "Cindy", "Aaron"])== {"Aaron", "Jane"})
print(MostCommonName_Onln(["Cindy"]) == "Cindy")
print(MostCommonName_Onln(["Jane", "Aaron", "Cindy"]) == {"Aaron","Cindy", "Jane"})
print(MostCommonName_Onln([]) == None)
print("#==============================================================================")

print("O(n)")
print(MostCommonName_On(["Jane", "Aaron", "Cindy", "Aaron"])== "Aaron")
print(MostCommonName_On(["Jane", "Aaron", "Jane", "Cindy", "Aaron"])== {"Aaron", "Jane"})
print(MostCommonName_On(["Cindy"]) == "Cindy")
print(MostCommonName_On(["Jane", "Aaron", "Cindy"]) == {"Aaron","Cindy", "Jane"})
print(MostCommonName_On([]) == None)
print("#==============================================================================")




