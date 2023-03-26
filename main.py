import json
import os
import re
from datetime import datetime
from tkinter import Tk, Menu, messagebox
from Controller.ActivityManager import ActivityManager
from Model.ActivityToJsonEncoder import ActivityToJsonEncoder


class NotAMinuteLongerApp:
    def __init__(self):
        self.search_for_saved_settings()
        self.search_for_recovery_files()
        self.root = Tk()
        self.am = ActivityManager(self.root)

        self.root.title("ActivityTracker")
        self.root.resizable(width="false", height="false")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        self.settings_menu = Menu(self.menubar, tearoff=0)
        self.settings_menu.add_command(label="Settings", command=self.open_settings)
        self.menubar.add_cascade(label="Settings", menu=self.settings_menu)

        self.root.mainloop()


    def search_for_saved_settings(self):
        pass

    def search_for_recovery_files(self):
        """searches for recovery files with today's activity."""
        current_dir = os.getcwd()
        # print(f"start searching in {current_dir}")
        recovery_filename = "tasks_" + datetime.now().strftime("%Y_%m_%d")
        # print(recovery_filename)
        files = [f for f in os.listdir(current_dir) if
                 os.path.isfile(f) and re.search("^" + recovery_filename + "[_0-9]*\.json", f)]
        if files:
            files.sort()
            messagebox.showinfo("Previous activity found!", f"Found a recovery file from today: {files.pop()}.")
            self.recover_activity_data()
        for f in files:
            print(f)

    def recover_activity_data(self):
        #TODO: expand this functionality
        print("recovering!")

    @staticmethod
    def create_file_name(self):
        return "tasks_"+datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+".json"

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            try:
                with open(self.create_file_name(), "w+") as file:
                    json_encoder = ActivityToJsonEncoder()
                    json_formatted = json.dumps(json.loads(json_encoder.encode(self.am)), indent=2)
                    file.write(json_formatted)
            except:
                messagebox.askokcancel("Ouć", "Something went terribly wrong, data will not be saved!")
            self.root.destroy()

    def open_settings(self):
        #TODO: develop this
        messagebox.askokcancel("Settings", "Settings menu will come here")


if __name__ == "__main__":
    app = NotAMinuteLongerApp()
