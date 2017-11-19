class animal:
    def eat(self):
        print("eating")

class cat(animal):
    def sound(self):
        print("meow")

class sleep(cat):
    def action(self):
        print("cat is sleeping")

s = sleep()
s.eat()
s.sound()
s.action()