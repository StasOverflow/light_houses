class HouseHold:

    def __init__(self):
        self.neighbour_list = list()
        self.power_plant_list = list()


class World:

    def create_power_plant(self):
        raise NotImplementedError("To be implemented")

    def create_household(self):
        raise NotImplementedError("To be implemented")

    def connect_household_to_power_plant(self, household, power_plant):
        raise NotImplementedError("To be implemented")

    def connect_household_to_household(self, household1, household2):
        raise NotImplementedError("To be implemented")

    def disconnect_household_from_power_plant(self, household, power_plant):
        raise NotImplementedError("To be implemented")

    def kill_power_plant(self, power_plant):
        raise NotImplementedError("To be implemented")

    def repair_power_plant(self, power_plant):
        raise NotImplementedError("To be implemented")

    def house_hold_has_electricity(self, household):
        raise NotImplementedError("To be implemented")
