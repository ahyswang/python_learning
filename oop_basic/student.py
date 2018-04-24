
# class
class Student(object):
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def print_name(self):
        print('%s:%s' % (self.__name, self.__age))

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
        
# for test
if __name__ == '__main__':
    stu_1 = Student('Bob', 18)
    stu_1.print_name()