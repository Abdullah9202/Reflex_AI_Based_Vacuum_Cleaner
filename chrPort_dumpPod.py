import tkinter as tk
from tkinter import ttk
import threading

# Class to create and manage the charging bar
class ChBar():
    def __init__(self) -> None:
        # Initializing the frame and progress bar outside to make it globally accessible
        self.frame = None
        self.progress_Bar = None
        self.progress_Var = None
    
    def initCharge(self):
        self.progress_Var.set(100)
    
    def chrPortProgressBar(self):
        # Main window
        self.frame = tk.Tk(screenName="Charging Progress bar")
        # Title
        self.frame.title(string="Battery")
        # Getting the monitor info
        screen_height = self.frame.winfo_screenheight()
        screen_width = self.frame.winfo_screenwidth()
        # Setting the Windows dimensions
        window_height = int(screen_height * 0.2)
        window_width = int(screen_width * 0.71)
        # Placing the frame
        self.frame.geometry(f"220x50+{window_width}+{window_height}")
        # Progress bar
        self.progress_Var = tk.DoubleVar(master=self.frame, value=100)
        self.progress_Bar = ttk.Progressbar(master=self.frame, mode="determinate", length=160, 
                                       orient="horizontal", variable=self.progress_Var)
        # Creating the lable_level
        self.label_lvl = tk.Label(self.frame, textvariable=self.progress_Var)
        # Placing the progress bar on frame
        self.progress_Bar.pack(pady=15)
        # Placing the label_lvl on frame
        self.label_lvl.pack()
        # Initializing the progress bar with 100%
        self.initCharge()

        # Schedule the function to update the progress bar after a delay
        # self.frame.after(100, self.updateCharge())
        self.frame.after(100, lambda: self.updateCharge(1))

        self.frame.mainloop()
        
    # Function to start threading for Progress bar
    def chrPortProgressBar_Threaded(self):
        # Creating a separate daemon thread for tkinter
        self.thread = threading.Thread(target=self.chrPortProgressBar, daemon=True)
        self.thread.start()
        
    # Function to decrease charging according to the steps taken
    def updateCharge(self, step_Taken):
        # Checking the steps taken and setting the percentages
        self.decr_Percentage = 0
        if step_Taken <= 50:
            self.decr_Percentage = 50 / 100
        elif step_Taken <= 100:
            self.decr_Percentage = 80 / 100
        elif step_Taken <= 250:
            self.decr_Percentage = 96 / 100
        else:
            self.decr_Percentage = 65 / 100
            
        # Decreasing the charge according to the steps taken
        self.progress_Var.set(self.progress_Var.get() - self.decr_Percentage)
        
        # Checking if the charge is less than 25%
        if self.progress_Var.get() <= 25:
            print("Danger! Going below the 25%")