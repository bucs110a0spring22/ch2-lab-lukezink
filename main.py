import random

#Part A
weeks = 16
print("Number of Weeks: "+str(weeks), type(weeks))
classes = 5
print("Number of classes: "+str(classes), type(classes))
tuition = 6000
print("The tuition is: "+str(tuition), type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("The cost per week is: "+ str(cost_per_week), type(cost_per_week))
classes_per_week = 10
print("The classes per week is: " + str(classes_per_week), type(classes_per_week))
cost_per_class = cost_per_week/classes_per_week
print("The cost per class is", str(cost_per_class), "dollars", type(cost_per_class))

#Part B
mylist = ["carrot", 69, "Barack Obama", 420, "cAPITALISM"]
randompick = random.choice(mylist)
print("Random pick: "+str(randompick))