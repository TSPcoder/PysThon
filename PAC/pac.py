import threading


def synchronised(method):
    def f(*args) :
        self = args[0]
        with self.lock:
            return method(*args)
        return f


class Observable:

    def __init__(self):
        self.lock = threading.RLock()
        self.changed = False
        self.observers = []

    @synchronised
    def has_changed(self):
        with self.lock:
            return self.changed

    @synchronised
    def set_changed(self):
         self.changed = True

    @synchronised
    def clear_changed(self):
         self.changed = False

    @synchronised
    def add_observer(self, observer):
         self.observers.append(observer)

    @synchronised
    def del_observer(self, observer):
         self.observers.remove(observer)

    @synchronised
    def notify_observers(self):
         for obs in self.observers:
             obs.update()
         self.clear_changed


class Observer :

    def update(self):
        """
        subclasses have to redefine this method
        """
        pass