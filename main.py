from turtle import Screen
from vacuum import vCleaner

# Screen
Frame = Screen()
# Title
Frame.title("Intelligent Vacuum Cleaner")
# Screen dimensions
Frame.setup(width=800, height=800)
# Creating an object of the vCleaner class
VCln = vCleaner()
# Creating a dumping pod in turtle frame
VCln.dumpingPod()
# Creating a charging port in turtle frame
VCln.chargingPort()
# Calling dirt function
VCln.createDirt(20)
# Creating vacuum cleaner
VCln.vacuumCleaner(9)
# Calling start cleaning function
VCln.startCleaning()

# Exit
Frame.exitonclick()