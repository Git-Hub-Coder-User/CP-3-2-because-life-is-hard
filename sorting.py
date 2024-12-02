#"Contain your PTSD, it's fine, I promise" - LaRose
#"Dictionaries are great" - LaRose
#"I'm so happy for you, I guess" - LaRose
#"Is Tia a real person" - LaRose
#"I hate Mac" - LaRose
#"I don't want to think" - LaRose
#"My mind is starting to cry" - Jonathan
#"I need more dictionaries" - LaRose
#"I function that utilizes an arrow" - LaRose
#"You're all fired" - LaRose
#"Your wages are totally fair, they're what you earn" - LaRose
#"It's almost like we want people are are helpful to society" - LaRose
#"Could I right now? Yes. Do I want to? No. " - LaRose
#"Why is this a conversation you're having? " - LaRose
#"That was just to build the employees" - LaRose
#"Was that to imply that they're not people? " - Jonathan "Only you" - LaRose
#"No rights. That's not a method they have. " - LaRose
#"Obviously we're returning electromagnetic pulses, how did you know? " - LaRose
#"There will be no sacrifices" - LaRose
#"The stars are not in position for this sacrifice" - LaRose
#"You guys don't know what that means and I'm not explaining" - LaRose
#"Can I get attrgetter? " - Jonathan
#"Why would you want to see this stuff? " - LaRose
#"A new topic I forgot. It's very important. " - LaRose
#"Okay, we're not going to talk about that" - LaRose

from operator import attrgetter

li = (9, 1, 8, 2, 7, 3, 6, 4, 5)
slist = sorted(li, reverse = True)
# print(slist)
# li.sort(reverse = True)
# print(li)

#sorted(data) works for tuples and other similair stuff
#Sort method just takes list that already existed, sorted method creates a new list
# Sort changes the actual data, sorted returns a copy

di = {"name": "Tia", "job": "Sales", "age": 28, "os": "Mac"}
sdi = sorted(di)
# print(f"Dictionary: {sdi}")

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return f"({self.name}, {self.age}, ${self.salary})"

e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)

employees = [e1, e2, e3]

# def e_sort(emp):
#     return emp.age

s_employees = sorted(employees, key = attrgetter("age"), reverse = True)

print(s_employees)