# An awesome class for representing time

try:
    import colorama
except ImportError:
    pass

class Time(object):
    
    def __init__(self, ui):
        """ui : str (user input)"""
        self.hour, self.minute, self.second = map(int, ui.split(':'))

    def __add__(self, ot):
	var=Time("00:00:00")
	var.second = (self.second+ot.second)%60 
	var.min = (self.minute+ot.minute)%60 + (self.second+ot.second)//60
	var.hour = (self.hour+ot.hour)%24 + (self.minute+ot.minute)//24
        return var

    def __mul__(self, ot):
        return NotImplementedError

    def __rmul__(self, ot):
        return NotImplementedError

    def __repr__(self):
        return "{0}h {1}m {2}s".format(self.hour, self.minutes, self.second)

    
