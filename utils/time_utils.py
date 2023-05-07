import time


def formatted_time(timeval: int) -> str:
    return time.strftime("%H:%M:%S", time.gmtime(timeval))

