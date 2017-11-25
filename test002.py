class Emp:
    num = 0

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.name = self.f_name + " " + self.l_name
        Emp.num += 1

    def email(self):
        return '{}.{}@gmail.com'.format(self.f_name,self.l_name)

    @classmethod
    def emp_id(cls, num):
        cls.emp_count = num


e1 = Emp("Sunny", "Deb")
e2 = Emp("Sunny", "Deb")
e1 = Emp("Sunny", "Deb")
print(e1.name)
print(e1.email())

print()