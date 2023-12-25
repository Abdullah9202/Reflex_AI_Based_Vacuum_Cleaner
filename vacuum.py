from chrPort_dumpPod import ChBar
from random import randint, choice
from turtle import Turtle
from time import sleep
import pandas as pd
import os

# Excel file path (+ Absolute Path)
EXCEL_FILE_PATH = os.path.abspath("Reports/my_Data.xlsx")

# X and Y Co-ordinates for 800 x 800 frame
MIN_X_COR = -350
MAX_X_COR = 350
MIN_Y_COR = -350
MAX_Y_COR = 350

class vCleaner:
    def __init__(self):
        self.dirt_List = [] # To store dirt objects
        self.dirt = 0 # To temporarily store the dirt object
        self.vacuum = None # Initialize vacuum cleaner as none
        self.movment_Angles = [0, 45, 90, 135, 180, 225, 270, 315, 360]
        # self.step_counter = 0 # To keep track of number of steps taken by turtle
        self.sensing_Radius = 150 # Sensing radius of vacuum cleaner
    
    # Function for creating the dirt
    def createDirt(self, dirt_Points): # This function will create 10 dirt points
        # Creating 10 dirt objects using for loop
        for x in range(dirt_Points):
            self.dirt = Turtle() # Assigining new dirt object
            self.dirt.hideturtle() # Hiding the dirt objects
            self.dirt.shape("circle") # Changing the dirt shape
            self.dirt.penup() # Lifting the pen up
            self.dirt.shapesize(0.5, 0.5, 0.5) # Changing the shape size
            self.dirt_List.append(self.dirt) # Appending into list

        # Moving the dirt to the random positons in 800 x 800 frame
        for x in range(dirt_Points):
            self.dirt_List[x].goto(randint(MIN_X_COR, MAX_X_COR), randint(MIN_Y_COR, MAX_Y_COR)) # Sending the dirt object to the random co-ordinates
            self.dirt_List[x].showturtle() # Un-hiding the dirt objects
        

    # Function for creating a vacuum cleaner
    def vacuumCleaner(self, vacuum_cleaner_Speed):
        # Creating a vacuum cleaner
        self.vacuum = Turtle()
        # Hiding the vacuum cleaner
        self.vacuum.hideturtle()
        # Size of vacuum cleaner
        self.vacuum.shapesize(3.5, 3.5, 3)
        # Setting up the speed
        self.vacuum.speed(vacuum_cleaner_Speed)
        # Lifting the pen up
        self.vacuum.penup()
        # Setting up a starting point
        self.vacuum.goto(MIN_X_COR, MIN_Y_COR)
        # Setting up a direction
        self.vacuum.left(90)
        # Unhiding the vacuum cleaner
        self.vacuum.showturtle()
        # # Speed of vacuum cleaner
        # self.vacuum.speed(1)
        
    # Function to create a chraging port
    def chargingPort(self):
        # Charging port object
        self.cPort = Turtle(shape="square", visible=False)
        # Color
        self.cPort.color("green")
        # Picking up the pen
        self.cPort.penup()
        # Size of Chraging Port
        self.cPort.shapesize(1, 1, 0.5)
        # Positioning the Chraging Port
        self.cPort.goto(350, 350)
        # Unhiding the turtle
        self.cPort.showturtle()
        
    # Function to create a dumping pod
    def dumpingPod(self):
        # Dumping pod object
        self.dPod = Turtle(shape="circle", visible=False)
        # Color
        self.dPod.color("red")
        # Picking up the pen
        self.dPod.penup()
        # Size of Chraging Port
        self.dPod.shapesize(2, 2, 2)
        # Positioning the Chraging Port
        self.dPod.goto(-350, 350)
        # Unhiding the turtle
        self.dPod.showturtle()
        
    # Function to start cleaning
    def startCleaning(self):
        # ===============================================
        # Creating an object of ChPort class            # 
        self.Charging_Bar = ChBar()                     # 
        # Creating the charging the progress bar        #
        self.Charging_Bar.chrPortProgressBar_Threaded() #
        # ===============================================
        
        # Checking if the "Reports" directory exists
        reports_Dir = os.path.dirname(EXCEL_FILE_PATH)
        if not os.path.exists(path=reports_Dir):
            # Creating a directory if doesn't exists
            os.makedirs(reports_Dir)
        
        # Checking if the excel file exists
        if os.path.exists(EXCEL_FILE_PATH):
            # Loading the file
            df = pd.read_excel(EXCEL_FILE_PATH)
        else:
            # Creating a new dataFrame if file doesn't exists
            df = pd.DataFrame(columns=["Dirt_Position", "Status"])
            df.to_excel(EXCEL_FILE_PATH, index=False)
        # self.vacuum.forward(100)
        while True:
            # Checking if any dirt remained
            if not self.dirt_List:
                break # Breaking out of the loop
            
            # Calculate the current position
            current_x = self.vacuum.xcor()
            current_y = self.vacuum.ycor()

            # Wall avoidance
            if (
                current_x <= MIN_X_COR
                or current_x >= MAX_X_COR
                or current_y <= MIN_Y_COR
                or current_y >= MAX_Y_COR
            ):
                # Calculate the angle to turn to remain within bounds
                angle_to_turn = self.vacuum.towards(0, 0)  # Point towards the center
                self.vacuum.setheading(angle_to_turn)  # Set the new heading
                self.vacuum.forward(50)  # Move forward to stay within bounds
                self.Charging_Bar.updateCharge(50)
                # self.step_counter += 50 # Counting the steps
            else:
                self.vacuum.forward(100)
                self.Charging_Bar.updateCharge(100)
                # self.step_counter += 100 # Counting the steps
                self.vacuum.setheading(choice(self.movment_Angles))
                
                
            # Calculating the distance between vacuum cleaner and dirt using for loop
            for dirt_L in self.dirt_List:
                distance = self.vacuum.distance(dirt_L)
                # Sensing the dirt from provided radius (In pixels)
                if distance <= self.sensing_Radius:
                    dirt_Pos = self.vacuum.towards(x=dirt_L.xcor(), y=dirt_L.ycor())
                    print(f"Dirt found at angle {dirt_Pos}. Moving towards it.")
                    # Adding the cleaned dirt postion to excel file
                    df = df._append({"Dirt_Position": dirt_Pos, "Status": "Cleaned"}, ignore_index=True)                    
                    # Changing the head direction in the direction of dirt
                    self.vacuum.setheading(dirt_Pos)
                    self.vacuum.forward(distance) # Moving towards the dirt
                    self.Charging_Bar.updateCharge(distance)
                    # self.step_counter += distance # Counting the steps
                    # Cleaning the dirt
                    self.dirt_List.remove(dirt_L) # Dirt removed from the list
                    print("Cleaning.")
                    sleep(1) # 1 sec delay for cleaning ==> Optional
                    dirt_L.hideturtle()
                    print("Dirt removed.")
                    
            # Saving the data to the excel file
            df.to_excel(EXCEL_FILE_PATH, index=False)
                