class call(object):
  count = 0
  def __init__(self, name, num, time, reason):
    self.id = call.count
    self.name = name
    self.num = num
    self.time = time
    self.reason = reason
    self.id = call.count = call.count + 1
  def display(self):
    print self.id
    print self.name
    print self.num
    print self.time
    print self.reason
    return self

class center(object):
  def __init__(self):
    self.call_list = []
  def add(self, added):
    self.added = added
    self.call_list.append(added)
    return self
  def getq(self):
    print len(self.call_list)
  def remove(self, removed):
    self.removed = removed
    self.call_list.remove(removed)
    return self
  # def qsize(self):
  #   for c in self.call_list:
  #     c.display

call_1 = call("tyler", "555-5554", "3:30", "tired")
call_2 = call("frank", "2222222", "4", "sick")
call_3 = call("Gert", "2342344", "4:30", "to talk")
callcenter = center()

# call_1.display()
print call_1.id
print call_2.id
print call_2.id
print call_3.id
callcenter.add(call_1)
callcenter.getq()
callcenter.add(call_2)
callcenter.getq()
callcenter.add(call_3)
callcenter.getq()
callcenter.remove(call_1).remove(call_2).getq()