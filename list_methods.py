#"Who here has used map here? " - LaRose
#"Numbers are hard today" - LaRose
#"My notes aren't noting" - LaRose
#"These are great new things" - LaRose
#"I'm not making up words! It's a thing! " - LaRose
#"I missed the modulo . . . " - LaRose
#"No, I'm just making a list of countries in South America" - LaRose
#"Why would you delete a country? " - Jonathan
#"We're going to look at it. And then you're probably never going to use it again" - LaRose
#"Don't convert it to a list. I'm a dummy" - LaRose

from functools import reduce

mylist = [4, 6, 8, 1, 5, 10, 7]
newlist = ["", "Aregentina", "", "Brazil", "Chile", "", "Columbia", "", "Ecuador", "", "", "Venezuela"]

# for num in mylist:
#     newlist.append(num + 1)

#Arguments for map are a function and a list to do the function to

def increase(num):
    return num + 1

# print(list(map(increase, mylist)))

def multiple(num):
    if num % 3 == 0:
        return num
    
# print(list(filter(multiple, mylist)))

#Lambda passed in: what happens
# print(list(filter(lambda num: num % 3 == 0, mylist)))

# print(list(filter("None", newlist)))
muliplier = lambda x, y: x * y

#reduce reducing a list into a single thing
print(reduce(muliplier, mylist))