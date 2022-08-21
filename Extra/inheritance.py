class Employee():
    def __init__(self, val, name):
        self.val = val
        self.name = name
    
    def PrintName(self):
        return self.name

class Freshers(Employee):
    def __init__(self, age):
        self.age = 12
        
class class2(Employee):
    pass


if __name__ == "__main__":
    emp = class2()
    