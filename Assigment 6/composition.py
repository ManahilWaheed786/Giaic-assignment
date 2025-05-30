class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        print("Car is starting...")
        self.engine.start()


# Example usage
if __name__ == "__main__":
    my_engine = Engine()
    my_car = Car(my_engine)
    my_car.start_car()
