import tkinter as tk
from tkinter import ttk
import threading

# Class to create and manage the charging bar
class ChBar():
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
        progress_Bar = ttk.Progressbar(master=self.frame, mode="determinate", length=160, orient="horizontal", variable="IntVar")
        # Placing the progress bar on frame
        progress_Bar.pack(pady=15)

        self.frame.mainloop()
        
    # Function to start threading for Progress bar
    def chrPortProgressBar_Threaded(self):
        # Creating a separate daemon thread for tkinter
        self.thread = threading.Thread(target=self.chrPortProgressBar, daemon=True)
        self.thread.start()