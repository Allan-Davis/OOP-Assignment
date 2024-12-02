class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand  # Brand of the smartphone
        self.model = model  # Model of the smartphone
        self.battery_life = battery_life  # Battery life in hours

    def make_call(self, number):
        print(f"Calling {number}...")

    def check_battery(self):
        print(f"Battery life: {self.battery_life} hours remaining.")

    def recharge(self):
        print("Recharging your smartphone...")
        self.battery_life = 100  # Reset battery to full

# Creating an object of Smartphone
my_phone = Smartphone("Apple", "iPhone 14", 80)

# Using the methods
my_phone.make_call("123-456-7890")
my_phone.check_battery()
my_phone.recharge()
my_phone.check_battery()
