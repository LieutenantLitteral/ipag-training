# An awesome class for representing time

try:
    import colorama
except ImportError:
    pass

class Time(object):
    
    def __init__(self, ui):
        """ui : str (user input)"""
        self.hour, self.minutes, self.second = ui.split(':')

    def __add__(self, ot):
        return NotImplementedError

    def __repr__(self):
        return NotImplementedError

    
