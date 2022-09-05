class Javatpoint:
   def __init__(self, age=49):
      self._age = age
# make the getter method
   def get_age(self):
      return self.__age
# make the setter method
   def set_age(self, a):
      self.__age = a
grad_obj = Javatpoint()
print(grad_obj._age)
# Before using setter
print(grad_obj.get_age())
# After using setter
grad_obj.set_age(2020)
print(grad_obj._age)
