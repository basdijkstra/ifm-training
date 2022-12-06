from abc import ABC

class Keyboard(ABC):
    pass

class Monitor(ABC):
    pass

class Computer:

    def __init__(self, keyboard: Keyboard, monitor: Monitor):
        self.keyboard = keyboard
        self.monitor = monitor

class StandardKeyboard(Keyboard):

    def __init__(self):
        pass

class StandardMonitor(Monitor):

    def __init__(self):
        pass
