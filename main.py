import random

#Part A
weeks = 16
print(weeks, type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type(cost_per_week))
classes_per_week = 10
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week/classes_per_week
print("The cost per class is", cost_per_class, "dollars")
print(cost_per_class, type(cost_per_class))

#Part B
mylist = ["carrot", 69, "Barack Obama", 420, "cAPITALISM"]
randompick = random.choice(mylist)
print(randompick)