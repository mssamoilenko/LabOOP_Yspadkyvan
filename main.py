#task1
class Device:
    current = False
    def __init__(self, manufacturer, model, year, volume, price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.volume = volume
        self.price = price

    def assembly(self):
        pass

    def work(self, current):
        self.current = current
        if current == True:
            return f"The device is ready for use."
        else:
            return f"Connect the device to the power supply."

printer = Device("Samsung", "FR-6", 1999, 0.5, "20$")
print(printer.work(False))