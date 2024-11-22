#"I already ruined everything" - LaRose
#"My lightsaber is my classroom pointer, it's not weird. " - LaRose
#"Yes, it's discrimination against big numbers and I'm lazy. " - LaRose
#"If you don't sanitize your inputs, I'll sanitize your life" - George
#"I sanitized the input; it's fine" - LaRose
#"Users love getting yelled at" - LaRose
#"People are stupid" - LaRose
#"It's your responsibility to keep them from breaking things with their stupidity" - LaRose
#"Tasers. Let's try that on you guys first. " - LaRose
#"Instead of waiting for an error to occur, we can raise errors ourselves" - LaRose
#"I need parantheses" - LaRose
#"I don't want my user to input the number seven cause it's lame" - LaRose

#Exceptions are how we deal with stupid users without breaking things
#Available easy errors: zero division, file not found, value error, type error, index error

class NegativeNumberError(Exception):
    pass

while True:
    try: 
        num = int(input("Tell me a number: "))
    except (ValueError, TypeError):
        print("That wasn't a whole number . . . ")
        continue
    else:
        break

while True:
    try: 
        numTwo = int(input("Tell me another number: "))
    except ValueError:
        print("That wasn't a whole number . . . ")
        continue
    else:
        try: 
            if numTwo <= 0:
                raise NegativeNumberError("Can't be a negative number")
            print(f"{str(num)} divided {str(numTwo)} equals {num / numTwo}. ")
        except ZeroDivisionError:
            print("You can't divide by zero or a negative")
        except NegativeNumberError as e:
            #e stands for error, it's the string we passed in
            print(e)
        else: 
            break
    finally:
        #Runs, no matter what (When it gets there)
        print("*Cue the obnoxious music*")