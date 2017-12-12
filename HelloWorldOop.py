
class HelloWorld(object):
    """docstring for HelloWorld"""
    def __init__(self, arg):
        super(HelloWorld, self).__init__()
        self.arg = arg
    @classmethod
    def hello(self):
        print("Hello World")

HelloWorld.hello()
