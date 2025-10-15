import pytest


from Homework_5_6 import Car, Bus, Bike
# def test_car_trip_cost():
#     niva = Car('Нива', 70, 6)
#     result = niva.trip_cost(100)
#     assert result == 10
#
# def test_bus_trip_cost():
#     bus = Bus('Mercedez', 50, 10)
#     result = bus.trip_cost(100)
#     assert result == 100 * 0.05 * 10
#

@pytest.mark.parametrize('vehicle, distance, expected_result',[

    (Car('Нива', 70, 6), 100, 10),
    (Bus('Mercedez', 50, 10), 100, 100*0.05*10)
                         ])
def test_vehicle_trip_cost(vehicle, distance, expected_result):
    vehicle = vehicle
    result = vehicle.trip_cost(distance)
    assert result == expected_result




#КОНТЕКСТНЫЙ МЕНЕДЖЕР!!!
