#task1
class Device:
    def __init__(self, manufacturer, model, year, volume, price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.volume = volume
        self.price = price
        self.current = False

    def power(self, state):
        self.current = state
        return "Device is now ON." if self.current else "Device is now OFF."

    def work(self):
        return "The device is ready for use." if self.current else "Connect the device to the power supply."

class CoffeeMachine(Device):
    def __init__(self, manufacturer, model, year, volume, price):
        super().__init__(manufacturer, model, year, volume, price)

    def check_assembly(self, first_part, second_part):
        if first_part == "Water Tank" and second_part == "Filter Basket":
            return "The coffee machine is ready to work."
        else:
            return "You have set the coffee machine incorrectly. It is not ready for use."

class Blender(Device):
    def __init__(self, manufacturer, model, year, volume, price):
        super().__init__(manufacturer, model, year, volume, price)

    def blend(self):
        if self.current:
            return "Blender is blending ingredients."
        else:
            return "Turn on the blender to start blending."

class MeatGrinder(Device):
    def __init__(self, manufacturer, model, year, volume, price):
        super().__init__(manufacturer, model, year, volume, price)

    def grind_meat(self):
        if self.current:
            return "Meat grinder is grinding meat."
        else:
            return "Turn on the meat grinder to start grinding."

printer = Device("Samsung", "FR-6", 1999, 0.5, "20$")
print(printer.work())
printer.power(True)
print(printer.work())

coffee_machine = CoffeeMachine("Siemens", "4556G", 2000, 30, "200$")
print(coffee_machine.check_assembly("Water Tank", "Filter Basket"))
print(coffee_machine.check_assembly("Filter Basket", "Filter Basket"))

blender = Blender("Philips", "BL-23", 2022, 1.5, "100$")
print(blender.blend())
blender.power(True)
print(blender.blend())

meat_grinder = MeatGrinder("Bosch", "MG-500", 2018, 0.8, "150$")
print(meat_grinder.grind_meat())
meat_grinder.power(True)
print(meat_grinder.grind_meat())