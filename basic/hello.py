# coding:utf-8
print "hello"

# list sample
classmates = ['Michel', 'Bob', 'Tracy']
print classmates
print classmates[0]
print classmates[1]
print classmates[2]

classmates.append('Adam')
print classmates
classmates.insert(1, 'Jack')
print classmates
classmates.pop()

# tuple 
classmates_1 = ('Michael', 'Bob', 'Tracy')
print classmates_1

# if 
age = 25
if age > 20:
    print 'your age is', age
    print 'adult'
else:
    print 'your age is', age
    print 'teenager'

# for 
names = ['Michal', 'Bob', 'Tracy']
for name in names:
    print name

# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

# dict
dict_1 = {'Michal': 95, 'Bob': 75, 'Tracy': 85}
print dict_1['Bob']
print dict_1.get('Bob1')

# set
set_1 = set([1,2,3,4])
print set_1

# function
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x 

print my_abs(8)
print my_abs(-10)


# class
class Student(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_name(self):
        print('%s:%s' % (self.name, self.age))

stu_1 = Student('Bob', 18)
stu_1.print_name()