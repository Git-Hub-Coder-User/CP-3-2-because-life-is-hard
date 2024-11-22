#They give me buggy code and it works just find - LaRose
#"You want to use Python One?!?!" - LaRose
#"Yeah, shut up" - LaRose
#"'Cause reasons" - LaRose
#"If it doesn't work, it's a nightmare" - LaRose
#"How to avoid debugging" - LaRose
#"We're not trying to make bugs" - LaRose
#"I hope it one day sinks in" - LaRose
#"So eventually you'll just get good" - Jonathan
#"I got a quote, yay " Jonathan
#"I haven't used a single colon or semioclon since fifth grade" - Jonathan
#"Hi. Let me have the code. " - LaRose
#"I don't do waiting"- LaRose

#This is Logging debugging
#The debugger is the play button with a bug symbol on the left; it can be slower, but it's useful enough when it works
import logging

logging.basicConfig(level = logging.DEBUG)
def buggy_function(a, b):
    result = a * b
    logging.debug(f"a: {a} b: {b} result: {result}")
    return result

#we could use an assert here
print(buggy_function(3, 3)) #Expected output: 6