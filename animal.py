class Animal(object):
  def __init__(self, name):
    self.name = name
    self.health = 100

  def walk(self):
    self.health -= 1
    return self

  def run(self):
    self.health -= 5
    return self

  def display_health(self):
    print "My name is " + str(self.name)
    print "My health is " + str(self.health)

animal1 = Animal("Ferdinand")
animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
  def __init__(self, name):
    super(Dog, self).__init__(name)
    self.health = 150

  def pet(self):
    self.health += 5
    return self

class Dragon(Animal):
  def __init__(self, name):
    super(Dragon, self).__init__(name)
    self.health = 170

  def fly(self):
    self.health -= 10
    return self

  def display_health(self):
    super(Dragon,self).display_health()
    print "I am a DRAGON!"
    return self

class Direwolf(Animal):
  def __init__(self, name):
    super(Direwolf, self).__init__(name)
    self.health = 165
  def devour(self):
    self.health += 10
    return self


Dragon1 = Dragon('Blackwing')
Dog1 = Dog("Sam")
Ghost = Direwolf("Ghost")

Ghost.devour().devour().display_health()
Dog1.walk().walk().walk().run().run().pet().display_health()
Dragon1.walk().fly().fly().display_health()
# Dog1.fly().display_health() -- Dog1 has no "fly" ability like we wanted