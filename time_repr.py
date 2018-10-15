# An awesome class for representing time

try:
    import colorama
except ImportError:
    pass

class Time(object):

    def __init__(self, user_input):
        """user_input : str (user input)"""
        self.hour, self.minute, self.second = user_input.split(':')

    def __add__(self, ot):
        return NotImplementedError

    def __mul__(self, ot):
        return NotImplementedError

    def __rmul__(self, ot):
        return NotImplementedError

    def __repr__(self):
        return "{0}h {1}m {2}s".format(self.hour, self.minutes, self.second)
