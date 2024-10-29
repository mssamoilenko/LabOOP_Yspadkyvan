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

#task2
class Ship:
    def __init__(self, name, year_built):
        self.name = name
        self.year_built = year_built
        self.is_operational = False

    def activate(self):
        self.is_operational = True
        return f"{self.name} is now active."

    def deactivate(self):
        self.is_operational = False
        return f"{self.name} is now deactivated."

    def status(self):
        status = "active" if self.is_operational else "inactive"
        return f"{self.name} (Year: {self.year_built}) is currently {status}."

class Frigate(Ship):
    def patrol(self):
        if self.is_operational:
            return f"{self.name} is patrolling the waters."
        return f"{self.name} is inactive and cannot patrol."

class Destroyer(Ship):
    def defend(self):
        if self.is_operational:
            return f"{self.name} is defending the fleet."
        return f"{self.name} is inactive and cannot defend."

class Cruiser(Ship):
    def attack(self):
        if self.is_operational:
            return f"{self.name} is attacking the target."
        return f"{self.name} is inactive and cannot attack."

frigate = Frigate("Simple Frigate", 2005)
destroyer = Destroyer("Simple Destroyer", 2010)
cruiser = Cruiser("Simple Cruiser", 2000)

print(frigate.activate())
print(frigate.patrol())
print(frigate.status())

print(destroyer.activate())
print(destroyer.defend())
print(destroyer.status())

print(cruiser.activate())
print(cruiser.attack())
print(cruiser.status())

#task3
class Money:
    exchange_rate = 0.027

    def __init__(self, whole=0, cents=0, currency='UAH'):
        self.whole = whole
        self.cents = cents
        self.currency = currency
        self.normalize()

    def set_whole(self, whole):
        self.whole = whole

    def set_cents(self, cents):
        self.cents = cents
        self.normalize()

    def normalize(self):
        if self.cents >= 100:
            extra_whole = self.cents // 100
            self.whole += extra_whole
            self.cents = self.cents % 100

    def display(self):
        return f"{self.whole}.{self.cents:02d} {self.currency}"

    def convert_to_usd(self):
        if self.currency == 'UAH':
            total_in_uah = self.whole + self.cents / 100
            dollars = total_in_uah * Money.exchange_rate
            return round(dollars, 2)
        else:
            raise ValueError("Конвертація доступна тільки для гривень.")

    def convert_to_uah(self):
        if self.currency == 'USD':
            total_in_usd = self.whole + self.cents / 100
            uah = total_in_usd / Money.exchange_rate
            return round(uah, 2)

    def show_bill(self):
        return f"Bill:\nAmount: {self.display()}\nTotal in UAH: {self.convert_to_uah() if self.currency == 'USD' else 'N/A'}\nTotal in USD: {self.convert_to_usd() if self.currency == 'UAH' else 'N/A'}"

money_uah = Money(100, 50, 'UAH')
print(money_uah.show_bill())
money_usd = Money(10, 0, 'USD')
print(money_usd.show_bill())