class mommy:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def printout(self):
        print(f'name is: {self.name}, age is: {self.age}')

mom  = mommy("irin", 35)

mom.printout()