from dispatcher import Dispatcher
from driver import Driver
from rider import Rider
from location import Location


def test_request_driver_no_available() -> None:
    """Test request_driver with no available driver."""
    d = Dispatcher()
    r1 = Rider('Bob', Location(0, 0), Location(0, 1), 100)
    d.request_driver(r1)
    assert d._waiting_riders[0] == r1

def test_request_driver_one_available() -> None:
    """Test request_driver with one available driver."""
    d = Dispatcher()
    d1 = Driver('Bobby', Location(0, 0), 1)
    d._available_drivers[d1.id] = d1
    r1 = Rider('Bob', Location(0, 0), Location(0, 1), 100)

    driver = d.request_driver(r1)
    assert driver == d1
    
def test_request_driver_available() -> None:
    """Test request_driver with many available driver."""
    d = Dispatcher()
    d1 = Driver('Bobby', Location(3, 1), 1)
    d2 = Driver('Mike', Location(1, 3), 2)
    d3 = Driver('Mico', Location(0, 0), 1)
    d4 = Driver('Michael', Location(2, 2), 2)
    d._available_drivers[d1.id] = d1
    d._available_drivers[d2.id] = d2
    d._available_drivers[d3.id] = d3
    d._available_drivers[d4.id] = d4

    r1 = Rider('Bob', Location(0, 0), Location(0, 1), 100)

    driver1 = d.request_driver(r1)
    assert driver1 == d3

def test_request_rider_initial() -> None:
    """Test request_rider initial."""
    d = Dispatcher()
    d1 = Driver('Bob', Location(0, 0), 1)
    d.request_rider(d1)
    assert d._available_drivers['Bob'] == d1

def test_request_rider_many() -> None:
    """Test request_rider for many requesting riders."""
    d = Dispatcher()
    d1 = Driver('Bob', Location(0, 0), 1)
    r1 = Rider('Bobby', Location(0, 0), Location(1, 1), 100)
    r2 = Rider('Bobby1', Location(0, 0), Location(1, 2), 100)
    r3 = Rider('Bobby2', Location(0, 0), Location(1, 3), 100)
    d._waiting_riders.extend([r1, r2, r3])

    rider = d.request_rider(d1)
    assert rider == r1

if __name__ == '__main__':
    import pytest
    pytest.main(['test_dispatcher.py'])