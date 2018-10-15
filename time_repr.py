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

        if self.hour > 24:
            raise ValueError("Not an appropriate hour (> 23)")
        
        if self.minute > 59:
            raise ValueError("Not an appropriate minute (> 59)")
        
        if self.second > 59:
            raise ValueError("Not an appropriate second (> 59)")

    def __eq__(self, ot):
        return (
            self.hour == ot.hour
            and self.minute == ot.minute
            and self.second == ot.second
        )

    def __add__(self, ot):
        time_result = Time("00:00:00")
        time_result.second = (self.second + ot.second) %60
        time_result.minute = ((self.minute + ot.minute) + (self.second + ot.second) // 60) %60
        time_result.hour = ((self.hour + ot.hour) + (self.minute + ot.minute) // 60) %24
        return time_result

    def __mul__(self, ot):
        return NotImplementedError

    def __rmul__(self, ot):
        return NotImplementedError

    def __repr__(self):
        return "{0}h {1}m {2}s".format(self.hour, self.minute, self.second)

