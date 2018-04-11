class MathDojo(object):
  def __init__(self, name):
    self.result = 0
    self.name = name
  def Add(self, *nums):
    for i in nums:
      if type(i) == list or type(i) == tuple:
        for k in i:
          self.result += k
      else:
        self.result += i
    return self
  def Subtract(self, *nums):
    for i in nums:
      if type(i) == list or type(i) == tuple:
        for k in i:
          self.result -= k
      else:
        self.result -= i
    return self

md = MathDojo("MD")
# print md.Add(2,3,4).Subtract(122, 65).Add(1,3).result
# print md.Add(2).Add(2,5).Subtract(3,2).result
print md.Add([1], 3,4).Add([3,5,7,8], [2,4.3,1.25]).Subtract(2, [2,3], [1.1,2.3]).result