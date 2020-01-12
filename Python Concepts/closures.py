# closure - ability of the returned inner function to remember outer function's scope.
# an example of closure.
def getMultiplier(a):
  def multiply(b):
    return a * b
# usage
multiplierOf5 = getMultiplier(5)
multiplierOf5(2) // Outputs 10.
