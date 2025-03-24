# https://launchschool.com/exercises/f87b95d5?track=python

class Banner:
    def __init__(self, message):
        self.message = message
        self.length = len(message)

    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self, message):
        self._message = message
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        self._length = length

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return f"| {' ' * self.length} |"

    def _horizontal_rule(self):
        return f"+-{'-' * self.length}-+"

    def _message_line(self):
        return f"| {self.message} |"
    
# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+