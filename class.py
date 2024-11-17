class Module:
  def __init__(self, name):
    self.name=name
  def s(self):
    print(self.name)
  def show(self, var):
    print(var)


apt = Module("apt")
apt.show("cia2o")
