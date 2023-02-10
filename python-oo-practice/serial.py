"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    # >>> serial = SerialGenerator(start=100)
    #
    # >>> serial.generate()
    # 100
    #
    # >>> serial.generate()
    # 101
    #
    # >>> serial.generate()
    # 102
    #
    # >>> serial.reset()
    #
    # >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """
        Make a new generate starting at 0
        """
        self.start = self.end = start

    def __repr__(self):
        """
        Show representation
        """
        return f"<SerialGenerator start= {self.start} end={self.end} >"

    def Add_start_end(self):
        """
        return next start
        """
        self.end += 1
        return self.end - 1

    def reset(self):
        """
        Reset start and end to original start.
        """
        self.end = self.start


print(SerialGenerator())
print(SerialGenerator())
