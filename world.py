class PowerPlant:

    def __init__(self, active=True):
        self.is_active = active

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, active):
        self._is_active = active
        return


class HouseHold:

    def __init__(self):
        self.neighbour_list = list()
        self.power_plant_list = list()

    @property
    def is_powered(self):
        if any(plant.is_active for plant in self.power_plant_list):
            return True
        elif any(neighbour.is_powered for neighbour in self.neighbour_list if neighbour is not self):
            return True
        else:
            return False

    def neighbour_add(self, neighbour):
        if neighbour not in self.neighbour_list:
            self.neighbour_list.append(neighbour)
            neighbour.neighbour_add(self)

    def neighbour_remove(self, neighbour):
        if neighbour in self.neighbour_list:
            self.neighbour_list.append(neighbour)
            neighbour.neighbour_remove(self)

    def power_plant_connect(self, plant):
        if plant not in self.power_plant_list:
            self.power_plant_list.append(plant)

    def power_plant_disconnect(self, plant):
        if plant in self.power_plant_list:
            self.power_plant_list.pop(plant)


class World:

    def create_power_plant(self):
        plant = PowerPlant()
        return plant

    def create_household(self):
        house = HouseHold()
        return house

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
        return household.is_powered
