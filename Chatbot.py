import time
import sys
import random
typing_speed = 150 #wpm
def write(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')
write("Hi\n")
time.sleep(2.5)
write("What is your name?\n")
name = input("User: ")
name = name.capitalize()
time.sleep(2.5)
print("Okay", name)
name = name + ': '
write("Artificial intellegence is taking over jobs, not jobs but tasks. But it is not a big problem becuase ai is making more new jobs that is has replaced.\nFor example, ai is taking 75 million jobs globally by 2022 but is creating 133 million. \nHowever, there are many people who are so worried about robots in fear they might take their jobs. \nIn fact, they can just get into the new jobs ai is creating or transact to other jobs which automation isn't taking over.\n")
time.sleep(2)
write("Do you understand what I said?\n")
time.sleep(1)
under = input(name)
under = under.lower()
if under == 'yes':
    write("Ok, good.\n")
elif under == 'no':
    write("Just wait; maybe you will understand in a few minutes.")
else:
    write("Never mind!\n")
time.sleep(2.5)

write("So, is artificial intellgince benefiting the humans?\nI will begin with the factories and the customers. Artificial intelligence and robots are benifiting factories and factories would want anything that produces with more\nefficiency.\nAnd costumers would want a better product and robots have efficiency because everytime they do exactly what they are programmed to do.\n But for some people like bus drivers or taxi drivers, ai might be afecting them in negative ways. In addition it might be very hard for them to transact between jobs.\nIn conclusion, it depends, but in my opinion ai is benefiting us alot.\n  ")
time.sleep(3)
write("Do you have any of these questions.\n 1- What is ai?\n 2- When will the main job will be gone ex, doctor?\n 3- What jobs are being made by ai?\n 4- Which jobs cannot be taken away?\n 5- Will it be harder to get a job because of Ai?\n 6- Which jobs are getting taken over by Ai?\n 7- What is the solution?\n 8- How do governments react with ai taking over jobs? \n")
write("Type the number of your chosen question.\n")
quest = eval(input(name))
if quest == 1:
    write("What is ai?\nArtificial intellegence, sometimes called machine intelligence, is intelligence demonstratod by machines. Which is programmad to do something as if it is a human.")
elif quest == 2:
    write("When will the main job will be gone ex, doctor?\nAi is replacing many jobs by 2022. But for doctors some say it might take until 2025. But maybe it is sooner than we think.")
elif quest == 3:
    write("What jobs are being made by ai?\nThere are going to be many software developers so they can progam robots. However, nobody know what jobs will ai create.")
elif quest == 4:
    write("Which jobs cannot be taken away?\nThese jobs have 0.4% of being automated: Audiologists, Emergency Management Directors, Sales Engineers, General Dentists, Psychologists and a few more.")
elif quest == 5:    
    write("Will it be harder to get a job because of Ai?\nNo, because ai is creating more jobs than it is replacing by 58 million jobs. But you have to enter jobs that are not high risk of automation. ")
elif quest == 6:
    write("Which jobs are getting taken over by Ai?\nArtificial intelligince is taking over repititive and simple jobs and any jobs that requires driving. \nEx. Truck drivers, judges, fast-food cooks, librarians, farmers, lumberjacks and many others.")
elif quest == 7:
    write("What is the solution?\nToday one of the most important questions you need to ask to kids, what do you want to be when you grow up? But maybe you will add to that what 5 jobs do you want when you grow up? \nAnd that is true, you tell him wether the job will be automated or not.")
elif quest == 8:
    write("How do governments react with ai taking over jobs?\nSeveral cities in Holland will give citizens a basic income about 1,000$ per month. \nBut in the USA citizens want big government help when robots and artificial intelligence take their jobs.")          
