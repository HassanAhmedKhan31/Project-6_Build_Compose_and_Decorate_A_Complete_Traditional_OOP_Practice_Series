class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

# Example
e = Engine()
c = Car(e)
c.start()
