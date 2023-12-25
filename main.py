from turtle import Screen
from vacuum import vCleaner
from chrPort_dumpPod import ChPort

# Screen
Frame = Screen()
# Title
Frame.title("Intelligent Vacuum Cleaner")
# Screen dimensions
Frame.setup(width=800, height=800)
# Creating an object of the class
VCln = vCleaner()
# Creating a charging port
VCln.dumpingPod()
# Creating a charging port
VCln.chargingPort()
# Calling dirt function
VCln.createDirt(20)
# Creating vacuum cleaner
VCln.vacuumCleaner(9)
# Calling start cleaning function
VCln.startCleaning()

# Exit
Frame.exitonclick()