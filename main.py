from turtle import Screen
from vacuum_Class import vCleaner

# Screen
Frame = Screen()
# Title
Frame.title("Intelligent Vacuum Cleaner")
# Screen dimensions
Frame.setup(width=800, height=800)
# Creating an object of the class
Obj1 = vCleaner()
# Creating a charging port
Obj1.chargingPort()
# Calling dirt function
Obj1.createDirt(20)
# Creating vacuum cleaner
Obj1.vacuumCleaner()
# Calling start cleaning function
Obj1.startCleaning()

# Exit
Frame.exitonclick()