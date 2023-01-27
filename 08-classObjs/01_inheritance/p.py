from n import sayhi
class hello(sayhi):
    def __init__(self):
        self.name="hello"
    def responds(self):
        print(' i am good')
        print('from hello class')
        print(f'my name is {self.name}')
obj=hello()
obj.responds()
obj.greeting()
