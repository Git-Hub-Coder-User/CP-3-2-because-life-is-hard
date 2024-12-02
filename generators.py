#"Don't delete things" - LaRose
#"Until my computer or runs out of space or the earth melts. Whatever happens first. " - LaRose
#"I am not dealing with answering these questions" - LaRose
#"Like really though, it's not even hard" - LaRose

#A generator is a prebuilt thing that allows you to create data
#Yield statements can be used to create generators

import itertools
import string

def nums():
    yield 1
    yield 2
    yield 3

# for x in nums():
#     print(x)

def letters():
    for c in string.ascii_lowercase:
        yield c

# for letter in letters():
#     print(letter)

def prime_numbers():
    yield 2
    prime_cache = [2]
    for n in itertools.count(3, 2):
        is_prime = True

        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_cache.append(n)
            yield n

# for p in prime_numbers():
#     print(p)
#     if p > 100:
#         break

squares = (x ** 2 for x in itertools.count(1))
print(type(squares))

for x in squares:
    print(x)
    if x > 1000:
        break