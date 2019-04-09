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

    def kill(self):
        # alias to is_active = False
        self.is_active = False

    def repair(self):
        # alias to is_active = True
        self.is_active = True


class HouseHold:

    def __init__(self):
        self.neighbour_list = list()
        self.power_plant_list = list()

    @property
    def is_connected_to_power_plant(self):
        if any(plant.is_active for plant in self.power_plant_list):
            return True

    def neighbour_has_power(self, asker):
        for neighbour in self.neighbour_list:
            if neighbour is not asker:
                if neighbour.is_connected_to_power_plant:
                    return True
                elif neighbour.neighbour_has_power(self):
                    return True
        return False

    def neighbour_add(self, neighbour):
        if neighbour not in self.neighbour_list:
            self.neighbour_list.append(neighbour)
            neighbour.neighbour_add(self)

    def neighbour_remove(self, neighbour):
        if neighbour in self.neighbour_list:
            self.neighbour_list.remove(neighbour)
            neighbour.neighbour_remove(self)

    def power_plant_connect(self, plant):
        if plant not in self.power_plant_list:
            self.power_plant_list.append(plant)

    def power_plant_disconnect(self, plant):
        if plant in self.power_plant_list:
            self.power_plant_list.remove(plant)


class World:

    def create_power_plant(self):
        plant = PowerPlant()
        return plant

    def create_household(self):
        house = HouseHold()
        return house

    def connect_household_to_power_plant(self, household, power_plant):
        household.power_plant_connect(power_plant)

    def connect_household_to_household(self, household1, household2):
        household1.neighbour_add(household2)

    def disconnect_household_from_power_plant(self, household, power_plant):
        household.power_plant_disconnect(power_plant)

    def kill_power_plant(self, power_plant):
        power_plant.kill()

    def repair_power_plant(self, power_plant):
        power_plant.repair()

    def house_hold_has_electricity(self, household):
        if household.is_connected_to_power_plant or household.neighbour_has_power(household):
            return True
        else:
            return False
