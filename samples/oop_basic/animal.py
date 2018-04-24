class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def  run(self):
        print('Cat is running...')

class Timer(object):
    def run(self):
        print('Start...')

if __name__ == '__main__':
    dog1 = Dog()
    dog1.run()
    cat1 = Cat()
    cat1.run()
    time1 = Timer()

    print isinstance(dog1, Animal)
    print isinstance(dog1, Dog)
    print isinstance(time1, Animal)