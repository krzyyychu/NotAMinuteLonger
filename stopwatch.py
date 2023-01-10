import tkinter
import time



class StopWatch(tkinter.Frame):
    """Simple stopwatch widget"""
    def __init__(self, parent=None, **kw):
        tkinter.Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = tkinter.StringVar()

        taskName = tkinter.Entry(self)
        taskName.pack(side=tkinter.LEFT)
        
        durationLabel = tkinter.Label(self, textvariable=self.timestr)
        self.__setTime(self._elapsedtime)
        durationLabel.pack(side=tkinter.LEFT)

        playButton = tkinter.Button(self, text="Start", command=self.start)
        playButton.pack(side=tkinter.LEFT)
        stopButton = tkinter.Button(self, text="Stop", command=self.stop)
        stopButton.pack(side=tkinter.LEFT)
    
    def __setTime(self, elapsed):
        """ Set the time string to Hours:Minutes:Seconds"""
        hours = int(elapsed/3600)
        minutes = int(elapsed/60 - hours*60.0)
        seconds = int(elapsed - minutes*60.0)                
        self.timestr.set('%02d:%02d:%02d' % (hours, minutes, seconds))    

    def __update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self.__setTime(self._elapsedtime)
        self._timer = self.after(1000, self.__update)  

    def start(self):
        """ Start the stopwatch, ignore if running. """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self.__update()
            self._running = True        
    
    def stop(self):
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self.__setTime(self._elapsedtime)
            self._running = False

root = tkinter.Tk()

root.title("ActivityTracker")
root.resizable(width="false", height="false")

continueSemaphor = False


def donothing():
    print("Donoting called")

def tick(taskDuration: tkinter.StringVar, offset=0):
    timer = 0
    continueSemaphor = True
    while continueSemaphor:
        time.sleep(1)
        timer += 1
        taskDuration.set(str(timer))



menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

sw1 = StopWatch(root)
sw1.pack()

sw2 = StopWatch(root)
sw2.pack()

sw3 = StopWatch(root)
sw3.pack()

sw4 = StopWatch(root)
sw4.pack()

sw5 = StopWatch(root)
sw5.pack()
# taskDuration = tkinter.StringVar()
# taskDuration.set("00:00")

# taskFrame = tkinter.Frame(root)
# taskName = tkinter.Entry(taskFrame).pack(side = tkinter.LEFT)
# taskDurationLabel = tkinter.Label(taskFrame, textvariable=taskDuration).pack(side = tkinter.LEFT)
# taskStart = tkinter.Button(taskFrame, text="Play", command=lambda : tick(taskDuration)).pack(side = tkinter.LEFT)
# taskStop = tkinter.Button(taskFrame, text="Stop").pack(side = tkinter.LEFT)




# taskFrame.pack()
if __name__ == "__main__":
    root.mainloop()
