from world import *


def test_no_electricity_by_default():
    world = World()
    house = world.create_household()
    assert world.house_hold_has_electricity(house) is False


def test_house_alive_with_pp():
    world = World()
    house = world.create_household()
    power_plant = world.create_power_plant()
    world.connect_household_to_power_plant(house, power_plant)
    assert world.house_hold_has_electricity(house) is True


def test_house_not_alive_with_pp_turned_off():
    world = World()
    house = world.create_household()
    power_plant = world.create_power_plant()
    world.connect_household_to_power_plant(house, power_plant)
    assert world.house_hold_has_electricity(house) is True
    world.disconnect_household_from_power_plant(house, power_plant)
    assert world.house_hold_has_electricity(house) is False


def test_house_is_alive_at_least_one_pp_connected():
    world = World()
    house = world.create_household()
    power_plant1 = world.create_power_plant()
    power_plant2 = world.create_power_plant()
    power_plant3 = world.create_power_plant()

    world.connect_household_to_power_plant(house, power_plant1)
    world.connect_household_to_power_plant(house, power_plant2)
    world.connect_household_to_power_plant(house, power_plant3)
    assert world.house_hold_has_electricity(house) is True

    world.disconnect_household_from_power_plant(house, power_plant1)
    assert world.house_hold_has_electricity(house) is True

    world.disconnect_household_from_power_plant(house, power_plant2)
    assert world.house_hold_has_electricity(house) is True

    world.disconnect_household_from_power_plant(house, power_plant3)
    assert world.house_hold_has_electricity(house) is False


def test_kill_one_pp():
    world = World()
    house = world.create_household()
    power_plant = world.create_power_plant()
    world.connect_household_to_power_plant(house, power_plant)
    assert world.house_hold_has_electricity(house) is True
    world.kill_power_plant(power_plant)
    assert world.house_hold_has_electricity(house) is False


def test_repaired_pp():
    world = World()
    house = world.create_household()
    power_plant = world.create_power_plant()
    world.connect_household_to_power_plant(house, power_plant)
    assert world.house_hold_has_electricity(house) is True
    world.kill_power_plant(power_plant)
    assert world.house_hold_has_electricity(house) is False
    world.repair_power_plant(power_plant)
    assert world.house_hold_has_electricity(house) is True


def test_few_houses_few_pp_case_one():
    world = World()
    house1 = world.create_household()
    house2 = world.create_household()
    power_plant1 = world.create_power_plant()
    power_plant2 = world.create_power_plant()
    world.connect_household_to_power_plant(house1, power_plant1)
    world.connect_household_to_power_plant(house1, power_plant2)
    world.connect_household_to_power_plant(house2, power_plant2)
    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is True
    world.kill_power_plant(power_plant2)
    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is False
    world.kill_power_plant(power_plant1)
    assert world.house_hold_has_electricity(house1) is False
    assert world.house_hold_has_electricity(house2) is False


def test_few_houses_few_pp_case_two():
    world = World()
    house1 = world.create_household()
    house2 = world.create_household()
    power_plant1 = world.create_power_plant()
    power_plant2 = world.create_power_plant()

    world.connect_household_to_power_plant(house1, power_plant1)
    world.connect_household_to_power_plant(house1, power_plant2)
    world.connect_household_to_power_plant(house2, power_plant2)
    world.disconnect_household_from_power_plant(house2, power_plant2)
    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is False
    world.kill_power_plant(power_plant2)
    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is False
    world.kill_power_plant(power_plant1)
    assert world.house_hold_has_electricity(house1) is False
    assert world.house_hold_has_electricity(house2) is False


def test_household_pp_case_one():
    world = World()
    house = world.create_household()
    power_plant = world.create_power_plant()
    assert world.house_hold_has_electricity(house) is False
    world.kill_power_plant(power_plant)
    world.connect_household_to_power_plant(house, power_plant)
    assert world.house_hold_has_electricity(house) is False


def test_two_houses_one_pp():
    world = World()
    house1 = world.create_household()
    house2 = world.create_household()
    power_plant = world.create_power_plant()
    world.connect_household_to_power_plant(house1, power_plant)
    world.connect_household_to_household(house1, house2)
    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is True
    world.kill_power_plant(power_plant)
    assert world.house_hold_has_electricity(house1) is False
    assert world.house_hold_has_electricity(house2) is False


def test_pp_house_house():
    world = World()
    house1 = world.create_household()
    house2 = world.create_household()
    house3 = world.create_household()

    power_plant = world.create_power_plant()
    world.connect_household_to_power_plant(house1, power_plant)
    world.connect_household_to_household(house1, house2)
    world.connect_household_to_household(house2, house3)

    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is True
    assert world.house_hold_has_electricity(house3) is True

    world.kill_power_plant(power_plant)

    assert world.house_hold_has_electricity(house1) is False
    assert world.house_hold_has_electricity(house2) is False
    assert world.house_hold_has_electricity(house3) is False

    world.repair_power_plant(power_plant)

    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is True
    assert world.house_hold_has_electricity(house3) is True

    world.disconnect_household_from_power_plant(house1, power_plant)

    assert world.house_hold_has_electricity(house1) is False
    assert world.house_hold_has_electricity(house2) is False
    assert world.house_hold_has_electricity(house3) is False


def test_two_houses_2_pp():
    world = World()
    house1 = world.create_household()
    house2 = world.create_household()
    power_plant1 = world.create_power_plant()
    power_plant2 = world.create_power_plant()
    world.connect_household_to_power_plant(house1, power_plant1)
    world.connect_household_to_power_plant(house2, power_plant2)

    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is True

    world.kill_power_plant(power_plant1)
    assert world.house_hold_has_electricity(house1) is False
    assert world.house_hold_has_electricity(house2) is True

    world.connect_household_to_household(house1, house2)

    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is True

    world.disconnect_household_from_power_plant(house2, power_plant2)

    assert world.house_hold_has_electricity(house1) is False
    assert world.house_hold_has_electricity(house2) is False


def test_pp_house_house_trail():
    world = World()
    house1 = world.create_household()
    house2 = world.create_household()
    house3 = world.create_household()
    house4 = world.create_household()
    house5 = world.create_household()

    power_plant = world.create_power_plant()
    world.connect_household_to_power_plant(house1, power_plant)
    world.connect_household_to_household(house1, house2)
    world.connect_household_to_household(house2, house3)
    world.connect_household_to_household(house3, house4)
    world.connect_household_to_household(house4, house5)

    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is True
    assert world.house_hold_has_electricity(house3) is True
    assert world.house_hold_has_electricity(house4) is True
    assert world.house_hold_has_electricity(house5) is True

    world.kill_power_plant(power_plant)

    assert world.house_hold_has_electricity(house1) is False
    assert world.house_hold_has_electricity(house2) is False
    assert world.house_hold_has_electricity(house3) is False
    assert world.house_hold_has_electricity(house4) is False
    assert world.house_hold_has_electricity(house5) is False

    world.repair_power_plant(power_plant)

    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is True
    assert world.house_hold_has_electricity(house3) is True
    assert world.house_hold_has_electricity(house4) is True
    assert world.house_hold_has_electricity(house5) is True

    world.disconnect_household_from_power_plant(house1, power_plant)

    assert world.house_hold_has_electricity(house1) is False
    assert world.house_hold_has_electricity(house2) is False
    assert world.house_hold_has_electricity(house3) is False
    assert world.house_hold_has_electricity(house4) is False
    assert world.house_hold_has_electricity(house5) is False


def test_pp_house_house_mix():
    world = World()
    house1 = world.create_household()
    house2 = world.create_household()
    house3 = world.create_household()
    house4 = world.create_household()
    house5 = world.create_household()

    power_plant = world.create_power_plant()
    world.connect_household_to_power_plant(house1, power_plant)
    world.connect_household_to_household(house1, house2)
    world.connect_household_to_household(house1, house3)
    world.connect_household_to_household(house1, house4)
    world.connect_household_to_household(house1, house5)
    world.connect_household_to_household(house2, house3)
    world.connect_household_to_household(house2, house4)
    world.connect_household_to_household(house2, house5)
    world.connect_household_to_household(house3, house4)
    world.connect_household_to_household(house3, house5)
    world.connect_household_to_household(house4, house5)

    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is True
    assert world.house_hold_has_electricity(house3) is True
    assert world.house_hold_has_electricity(house4) is True
    assert world.house_hold_has_electricity(house5) is True

    world.kill_power_plant(power_plant)

    assert world.house_hold_has_electricity(house1) is False
    assert world.house_hold_has_electricity(house2) is False
    assert world.house_hold_has_electricity(house3) is False
    assert world.house_hold_has_electricity(house4) is False
    assert world.house_hold_has_electricity(house5) is False

    world.repair_power_plant(power_plant)

    assert world.house_hold_has_electricity(house1) is True
    assert world.house_hold_has_electricity(house2) is True
    assert world.house_hold_has_electricity(house3) is True
    assert world.house_hold_has_electricity(house4) is True
    assert world.house_hold_has_electricity(house5) is True

    world.disconnect_household_from_power_plant(house1, power_plant)

    assert world.house_hold_has_electricity(house1) is False
    assert world.house_hold_has_electricity(house2) is False
    assert world.house_hold_has_electricity(house3) is False
    assert world.house_hold_has_electricity(house4) is False
    assert world.house_hold_has_electricity(house5) is False
