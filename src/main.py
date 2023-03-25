import json
from datetime import datetime
from tkinter import Tk, messagebox
from src.Controller.ActivityManager import ActivityManager
from src.Model.ActivityToJsonEncoder import ActivityToJsonEncoder

root = Tk()
am = ActivityManager(root)


def create_file_name():
    return "tasks_"+datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+".json"

def on_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        try:
            with open(create_file_name(), "w+") as file:
                json_encoder = ActivityToJsonEncoder()
                json_formatted = json.dumps(json.loads(json_encoder.encode(am)), indent=2)
                file.write(json_formatted)
        except:
            messagebox.askokcancel("Ouć", "Something went terribly wrong, data will not be saved!")
        root.destroy()


def main():
    root.title("ActivityTracker")
    root.resizable(width="false", height="false")
    root.protocol("WM_DELETE_WINDOW", on_close)

    root.mainloop()


if __name__ == "__main__":
    main()
