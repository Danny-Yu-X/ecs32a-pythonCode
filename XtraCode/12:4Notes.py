class Counter():
    def __init__(self):
        self.counter = 0
    def count(self):
        self.counter = self.counter + 1
    def reset(self):
        self.counter = 0
    def get_count(self):
        return self.counter

c = Counter()
print(type(c))
print("Count:", c.get_count())
print("Increment")
c.count()
print("Count:", c.get_count())
print("Increment")
c.count()
print("Count:", c.get_count())
print("Increment")
c.count()
print("Count:", c.get_count())
print("Increment")
c.count()
c.reset()
print("Reset Count", c.get_count())
