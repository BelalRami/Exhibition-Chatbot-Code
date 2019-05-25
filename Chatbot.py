import time
import sys
import random
import datetime
from termcolor import colored, cprint

typing_speed = 150 #wpm
input_sequence = ""

def write(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')

def input_and_save(prompt, label, indent = False):
    global input_sequence
    x = input(prompt)
    indentation_str = '   ' if indent == True else ''
    input_sequence = input_sequence + indentation_str + label + ": " + x + "\n"
    return x

def persist_input():
    global input_sequence
    currentDT = datetime.datetime.now()
    with open("feedback.txt", "a") as feedback_file:
        input_sequence = input_sequence + "Session ended at " + currentDT.strftime("%Y-%m-%d %H:%M:%S") + "\n\n\n"
        feedback_file.write(input_sequence)
    
time.sleep(3)    
write("Hi\n")
time.sleep(2.5)
write("What is your name?\n")
currentDT = datetime.datetime.now()
name = input_and_save("User: ", "Session at " + currentDT.strftime("%Y-%m-%d %H:%M:%S"))
name = name.capitalize()
time.sleep(2.5)
print("Okay, ", name)
cprint('\nJames Everleigh', 'red', attrs=['blink'])
name = name + ': '
write("Artificial intellegence is taking over jobs, not jobs but tasks. But it is not a big problem becuase AI is making more new jobs that is has replaced.\nFor example, AI is taking 75 million jobs globally by 2022 but is creating 133 million. \nHowever, there are many people who are so worried about robots in fear they might take their jobs. \nIn fact, they can just get into the new jobs AI is creating or transact to other jobs which automation isn't taking over.\n")
time.sleep(2)
write("Do you understand what I said?\n")
time.sleep(1)
under = input_and_save(name, "Understands Response", True)
under = under.lower()
if under == 'yes':
    write("Ok, good.\n")
elif under == 'no':
    write("Just wait; maybe you will understand in a few minutes.")
elif under == 'sure':
    write("Ok, good.\n")
else:
    write("Never mind!\n")
time.sleep(2.5)

write("So, is artificial intellgince benefiting the humans?\nI will begin with the factories and the customers. Artificial intelligence and robots are benifiting factories and factories would want anything that produces with more\nefficiency.\nAnd costumers would want a better product and robots have efficiency because everytime they do exactly what they are programmed to do.\nBut for some people like bus drivers or taxi drivers, AI might be afecting them in negative ways. In addition it might be very hard for them to transact between jobs.\nIn conclusion, it depends, but in my opinion AI is benefiting us alot.\n  ")

introMessage = "\nDo you have any of these questions?\n"
sayQuestions = True

while True:
    if sayQuestions == True:
        time.sleep(4)
        write(introMessage)
        write(" 1- What is AI?\n 2- When will the main job will be gone ex, doctor?\n 3- What jobs are being made by AI?\n 4- Which jobs cannot be taken away?\n 5- Will it be harder to get a job because of AI?\n 6- Which jobs are getting taken over by AI?\n 7- What is the solution?\n 8- How do governments react with AI taking over jobs? \n")
        write("Type the number of your chosen question\n")

    quest = input_and_save(name, "Questions Response", True)
    quest = quest.lower()
    sayQuestions = True
    introMessage = "\nDo you still have any of these questions?.\n"
    
    if quest == "1":
        write("What is AI?\nArtificial intellegence, sometimes called machine intelligence, is intelligence demonstratod by machines. Which is programmad to do something as if it is a human.")
    elif quest == "2":
        write("When will the main job will be gone ex, doctor?\nAi is replacing many jobs by 2022. But for doctors some say it might take until 2025. But maybe it is sooner than we think.")
    elif quest == "3":
        write("What jobs are being made by AI?\nThere are going to be many software developers so they can progam robots. However, nobody know what jobs will AI create.")
    elif quest == "4":
        write("Which jobs cannot be taken away?\nThese jobs have 0.4% of being automated: Audiologists, Emergency Management Directors, Sales Engineers, General Dentists, Psychologists and a few more.")
    elif quest == "5":    
        write("Will it be harder to get a job because of AI?\nNo, because AI is creating more jobs than it is replacing by 58 million jobs. But you have to enter jobs that are not high risk of automation. ")
    elif quest == "6":
        write("Which jobs are getting taken over by AI?\nArtificial intelligince is taking over repititive and simple jobs and any jobs that requires driving. \nEx. Truck drivers, judges, fast-food cooks, librarians, farmers, lumberjacks and many others.")
    elif quest == "7":
        write("What is the solution?\nToday one of the most important questions you need to ask to kids, what do you want to be when you grow up? But maybe you will add to that what 5 jobs do you want when you grow up? \nAnd that is true, you tell him wether the job will be automated or not.")
    elif quest == "8":
        write("How do governments react with AI taking over jobs?\nSeveral cities in Holland will give citizens a basic income about 1,000$ per month. \nBut in the USA citizens want big government help when robots and artificial intelligence take their jobs.")          
    elif quest == "no":
        write("Okay")
        time.sleep(2.5)
        break
    else:
        write("Please choose a question from 1-8 or say No if you do not have any questions!\n")
        sayQuestions = False
        time.sleep(2.5)
write("Was this helpful?\n")
write("Note# This is a yes or no question.\n")
helpful = input_and_save(name, "Helpful Response", True)
time.sleep(2.5)
helpful = helpful.lower()
if helpful == 'yes':
    pass
elif helpful == 'no':
    write("Can you say why?\n")
    nothelpful = input_and_save(name, "Why Not Helpful", True)
    time.sleep(2.5)
write("What did you like the most in our booth.\n")
likemost = input_and_save(name, "Liked Most", True)
time.sleep(2.5)
write("How do you think we can improve?\n")
improve = input_and_save(name, "Improvement Suggestions", True)
time.sleep(2.5)
write("Ok, thanks.\nGoodbye.")
persist_input()
time.sleep(10)    
 
