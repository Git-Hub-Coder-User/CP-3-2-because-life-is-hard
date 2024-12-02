#"Total witchcraft, absolutely" - LaRose
#"Yes, like a candy rapper" - LaRose

#Decoraters have a @ before them and change the function without changing the contents of the functions, "add-ons"

def cough(func):
    def func_wrapper():
        #stuff that happens before the function
        print("*cough*")

        func()
        #stuff that happens after the function
        print("*cough*")
    return func_wrapper

@cough
def awkward():
    print("Can I get a discount? ")

@cough
def answer():
    print("Sir, this is a dollar tree . . . ")

awkward()
answer()