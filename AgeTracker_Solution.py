class AgeTracker():

    def __init__(self):
        self.ages = {}

    def add_person(self, name, age):
        self.ages[name] = age

    def remove_person(self, name):
        del self.ages[name]

    def have_birthday(self, name):
        self.ages[name] += 1

    def get_birthday(self, name):
        if name in self.ages:
            return self.ages[name]
        else:
            return -1

ages = AgeTracker()
ages.add_person("Alice", 12)
ages.add_person("Bob", 19)
ages.add_person("Carol", 80)
ages.have_birthday("Bob")
ages.remove_person("Carol")
ages.get_birthday("Alice") # Should return 12
ages.get_birthday("Bob") # Should return 20
ages.get_birthday("Carol") # Should return -1
