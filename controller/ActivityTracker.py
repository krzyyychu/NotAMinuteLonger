from pynput import mouse, keyboard
from time import sleep
from threading import Thread


class ActivityTracker:
    '''
    Simple class to track user keyboard and mouse events.
    Args:
        inactivity_period - how many seconds user was idle before invoking inactivity_callback
        tick_callback - callback called every second when user is treated as active
    '''
    def __init__(self,
                 inactivity_period,
                 tick_callback):
        self.inactivity_period = inactivity_period
        self.elapsed_time = 0
        self._user_active = False
        self._tracker_activated = False

        self.tick_callback = tick_callback

        mouse_listener = mouse.Listener(
            on_move=self.user_event,
            on_click=self.user_event,
            on_scroll=self.user_event
        )
        keyboard_listener = keyboard.Listener(
            on_press=self.user_event,
            on_release=self.user_event
        )
        mouse_listener.start()
        keyboard_listener.start()
        self.timer = Thread(target=self._track_time, daemon=True)
        self.timer.start()

    def user_event(self, *args):
        self._user_active = True
        self.elapsed_time = 0

    def _track_time(self):
        """Method used by daemon thread, do not call"""
        while True:
            sleep(1)
            if self._tracker_activated:
                if self._user_active:
                    self.tick_callback()
                self.elapsed_time += 1
                if self.elapsed_time >= self.inactivity_period and self._user_active is True:
                    self._user_active = False
                    self.elapsed_time = 0
                #    self.inactivity_callback()

    def activate(self):
        self._tracker_activated = True

    def deactivate(self):
        self._tracker_activated = False


def tick():
    print("tick")


if __name__ == "__main__":
    at = ActivityTracker(3, tick)
    print("ActivityTracker set up: inactive")
    sleep(20)
