from pynput import mouse, keyboard
from time import sleep
from threading import Thread


class ActivityTracker:

    def __init__(self, inactivity_period, on_activity_func, on_inactivity_func):
        self.inactivity_period = inactivity_period
        self.elapsed_time = 0
        self.active = True
        self.on_activity = on_activity_func
        self.on_inactivity = on_inactivity_func
        mouse_listener = mouse.Listener(
            on_move = self.user_event,
            on_click = self.user_event,
            on_scroll = self.user_event
        )
        keyboard_listener = keyboard.Listener(
            on_press=self.user_event,
            on_release=self.user_event
        )
        mouse_listener.start()
        keyboard_listener.start()
        self.timer = Thread(target=self.track_time, daemon=True)
        self.timer.start()

    def user_event(self, *args):
        if not self.active:
            self.on_activity()
        self.active = True
        self.elapsed_time = 0

    def track_time(self):
        while True:
            sleep(1)
            self.elapsed_time += 1
            if self.elapsed_time >= self.inactivity_period and self.active is True:
                self.active = False
                self.elapsed_time = 0
                self.on_inactivity()


def active():
    print("activated")

def inactive():
    print("inactivated")

if __name__ == "__main__":
    at = ActivityTracker(3, active, inactive)
    print("ActivityTracker set up")
    sleep(40)
