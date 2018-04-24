
# class
class Student(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_name(self):
        print('%s:%s' % (self.name, self.age))

# for test
if __name__ == '__main__':
    stu_1 = Student('Bob', 18)
    stu_1.print_name()