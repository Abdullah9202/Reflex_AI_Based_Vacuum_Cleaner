from random import randint, choice
from turtle import Turtle
from time import sleep
import pandas as pd
import os

# Excel file path
EXCEL_FILE_PATH = "Code/Reports/my_Data.xlsx"

# X and Y Co-ordinates for 800 x 800 frame
MIN_X_COR = -350
MAX_X_COR = 350
MIN_Y_COR = -350
MAX_Y_COR = 350

class V_Cleaner:
    def __init__(self):
        self.dirt_List = [] # To store dirt objects
        self.dirt = 0 # To temporarily store the dirt object
        self.vacuum = None # Initialize vacuum cleaner as none
        self.movment_Angles = [0, 45, 90, 135, 180, 225, 270, 315, 360]
    
    # Function for creating the dirt
    def create_Dirt(self, dirt_Points): # This function will create 10 dirt points
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
    def vacuum_Cleaner(self):
        # Creating a vacuum cleaner
        self.vacuum = Turtle()
        # Hiding the vacuum cleaner
        self.vacuum.hideturtle()
        # Size of vacuum cleaner
        self.vacuum.shapesize(3.5, 3.5, 3)
        # Setting up the speed
        self.vacuum.speed(4)
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
        
        
    # Function to start cleaning
    def start_Cleaning(self):
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
            else:
                self.vacuum.forward(100)
                self.vacuum.setheading(choice(self.movment_Angles))
                
                
            # Calculating the distance between vacuum cleaner and dirt using for loop
            for dirt_L in self.dirt_List:
                distance = self.vacuum.distance(dirt_L)
                # Sensing the dirt from 150 pixels radius
                if distance <= 150:
                    dirt_Pos = self.vacuum.towards(dirt_L)
                    print(f"Dirt found at angle {dirt_Pos}. Moving towards it.")
                    # Adding the cleaned dirt postion to excel file
                    df = df._append({"Dirt_Position": dirt_Pos, "Status": "Cleaned"}, ignore_index=True)                    
                    # Changing the head direction in the direction of dirt
                    self.vacuum.setheading(dirt_Pos)
                    self.vacuum.forward(distance) # Moving towards the dirt
                    # Cleaning the dirt
                    self.dirt_List.remove(dirt_L) # Dirt removed from the list
                    print("Cleaning.")
                    sleep(1) # 1 sec delay for cleaning ==> Optional
                    dirt_L.hideturtle()
                    print("Dirt removed.")
                    
            # Saving the data to the excel file
            df.to_excel(EXCEL_FILE_PATH, index=False)
                