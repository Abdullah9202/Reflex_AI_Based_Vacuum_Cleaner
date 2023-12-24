from turtle import Screen
from vacuum_Class import V_Cleaner

# Screen
Frame = Screen()
# Title
Frame.title("Intelligent Vacuum Cleaner")
# Screen dimensions
Frame.setup(width=800, height=800)
# Creating an object of the class
Obj1 = V_Cleaner()
# Calling dirt function
Obj1.create_Dirt(20)
# Creating vacuum cleaner
Obj1.vacuum_Cleaner()
# Calling start cleaning function
Obj1.start_Cleaning()

# Exit
Frame.exitonclick()