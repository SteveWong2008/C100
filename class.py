class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
    

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelerating")

    def change_gear(self, gear_type):
        print("gear changed")

audi = Car("A6", "red", "Audi", 80)
print(audi.start)

