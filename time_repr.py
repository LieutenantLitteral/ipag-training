# An awesome class for representing time

try:
    import colorama
except ImportError:
    pass

class Time(object):

    def __init__(self, user_input):
        """Init method for the class.
        
        Parameters
        ==========
        
            user_input (str): user input; two-digit hour, two-digit minutes, and 
                two-digit seconds, all separated by colons (":").
        """
        if not isinstance(user_input, str):
            raise TypeError("Please input str only")
        self.hour, self.minute, self.second = map(int, user_input.split(':'))

    def __add__(self, ot):
        return NotImplementedError

    def __mul__(self, ot):
        return NotImplementedError

    def __rmul__(self, ot):
        return NotImplementedError

    def __repr__(self):
        return "{0}h {1}m {2}s".format(self.hour, self.minutes, self.second)
