class patient(object):
  id = 1
  def __init__(self, name, allg):
    self.name = name
    self.allg = allg
    for i in range(1, 501):
      self.bed_num = patient.id
  
class hospital(object):
  def __init__(self, name, capacity):
    self.patients = []
    self.name = name
    self.capacity = capacity
  def admit(self, admitted):
    self.admitted = admitted
    self.patients.append(admitted)
    if self.capacity <= len(self.patients):
      print "You're not welcome here"
  def discharge(self, discharged):
    self.discharge = discharged
    self.patients.remove(discharged)
  def hospinfo(self):
    # self.hosp = hosp
    print self.name
    print self.capacity
    print len(self.patients)

swedish = hospital("Swedish", 500)
patient0 = patient("tyler", "none")
swedish.admit(patient0)
swedish.hospinfo()