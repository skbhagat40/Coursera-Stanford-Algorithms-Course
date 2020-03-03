# Example of generator using yield.
# yield preserves the state.
# refer demo implementation.py


def get_ten_nos():
    counter = 0
    while counter < 10:
        yield counter
        counter += 1


for i in get_ten_nos():
    print("number fetched is {}".format(i))

# we can see yield as a way of interchange of control.
"""
This can be useful in situation were we have certain functions in an api and we want to make sure that
user calls some methods in succession.
Let's see an example implementation.
"""


class Api:
    def func1(self):
        print("func1 is being called")

    def func2(self):
        print("func2 is being called")

    def func3(self):
        print("func3 is being called")

    #
    # def __call__(self, *args, **kwargs):
    #     yield self.func1()
    #     yield self.func2()
    #     yield self.func3()
    def api(self):
        yield self.func1()
        yield self.func2()
        yield self.func3()


a = Api()
api_obj = a.api()
api_obj.__next__()
api_obj.__next__()
api_obj.__next__()
#
# a().__next__()
# # do some processing
# a().__next__()
# # do some processing
# a().__next__()
# # do some processing
"""
We get the following output 
func1 is being called
func2 is being called
func3 is being called
"""
