class LifeSupportSystem:
    def __init__(self, oxygen_supply, water_supply, food_supply, waste_storage):
        self.oxygen_supply = oxygen_supply
        self.water_supply = water_supply
        self.food_supply = food_supply
        self.waste_storage = waste_storage

    def consume_resources(self, oxygen_rate, water_rate, food_rate):
        self.oxygen_supply -= oxygen_rate
        self.water_supply -= water_rate
        self.food_supply -= food_rate

    def produce_waste(self, waste_rate):
        self.waste_storage += waste_rate

    def check_supply_levels(self):
        if self.oxygen_supply <= 0:
            print("Oxygen supply is low.")
        if self.water_supply <= 0:
            print("Water supply is low.")
        if self.food_supply <= 0:
            print("Food supply is low.")
        if self.waste_storage >= 1:
            print("Waste storage is full.")

    def update_supply_levels(self, oxygen_rate, water_rate, food_rate, waste_rate):
        self.consume_resources(oxygen_rate, water_rate, food_rate)
        self.produce_waste(waste_rate)
        self.check_supply_levels()

# Example usage:
lss = LifeSupportSystem(1000, 500, 100, 0)
lss.update_supply_levels(10, 5, 2, 1)
