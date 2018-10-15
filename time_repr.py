# An awesome class for representing time

try:
    import colorama
except ImportError:
    pass




class Time(object):
    
    def __init__(self, ui):
        """ui : str (user input)"""
        self.hour, self.minute, self.second = ui.split(':')

        if self.hour > 24 :
            raise ValueError("Not an appropriate hour (dumbass)")
        if self.minute > 59 :
            raise ValueError("Not an appropriate minute (dickhead)")
        if self.second > 59 :
            raise ValueError("Not an appropriate second (retarded)")

    def __add__(self, ot):
        return NotImplementedError

    def __mul__(self, ot):
        return NotImplementedError

    def __rmul__(self, ot):
        return NotImplementedError

    def __repr__(self):
        return "{0}h {1}m {2}s".format(self.hour, self.minutes, self.second)

    
