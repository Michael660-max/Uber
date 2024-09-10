from driver import Driver
from rider import Rider
from location import Location

def test_driver_initializer() -> None:
    """Testing the initializer for the driver."""
    l1 = Location(1,1)
    driver = Driver('bob', l1, 2)
    assert driver.id == 'bob'
    assert driver.location == l1
    assert driver.is_idle 
    assert driver._destination == None
    assert driver.speed == 2

def test_str() -> None:
    """Testing the __str__ for the driver."""
    l1 = Location(1,1)
    driver = Driver('bob', l1, 2)
    assert type(str(driver)) == str

def test_eq() -> None:
    """Testing the __eq__ for the driver."""
    l1 = Location(1,1)
    driver1 = Driver('boby', l1, 2)

    l2 = Location(1,1)
    driver2 = Driver('boby', l1, 2)

    assert driver1 == driver2

def test_get_travel_time() -> None:
    """Testing getting travel time for the driver."""
    l1 = Location(1, 1)
    l2 = Location(2, 2)
    driver1 = Driver('boby', l1, 2)
    time = driver1.get_travel_time(l2)
    assert time == 1

def test_start_drive() -> None:
    """Testing starting drive."""
    l1 = Location(1, 1)
    l2 = Location(2, 2)
    driver1 = Driver('boby', l1, 2)
    time = driver1.start_drive(l2)

    assert time == 1    
    assert driver1.is_idle == False
    assert driver1.location == l2

def test_end_drive() -> None:
    """Testing ending drive."""
    l1 = Location(1, 1)
    driver1 = Driver('boby', l1, 2)
    time = driver1.end_drive()
    
    assert time == None
    assert driver1.is_idle

def test_start_ride() -> None:
    """Testing starting ride."""
    # Environmental Setup
    l1 = Location(1, 1)
    l2 = Location(4, 2)
    l3 = Location(5, 4)

    driver1 = Driver('boby', l1, 2)
    rider1 = Rider('bob', 100, l2, l3)

    driver1.start_drive(l2)
    driver1.end_drive()
    result3 = driver1.start_ride(rider1)
    
    # Testing
    assert driver1.is_idle == False
    assert driver1._destination == l3
    assert rider1.status == 'satisfied'
    assert result3 == round(3 / 2)

def test_end_ride() -> None:
    """Testing ending ride."""
    # ES
    l1 = Location(1, 1)
    l2 = Location(4, 2)
    l3 = Location(5, 4)

    driver1 = Driver('boby', l1, 2)
    rider1 = Rider('bob', 100, l2, l3)

    driver1.start_drive(l2)
    driver1.end_drive()
    driver1.start_ride(rider1)
    driver1.end_ride()

    assert driver1.location == l3
    assert driver1.is_idle == True

def test_removing_destination() -> None:
    """Testing removing the destination of the driver."""
    l1 = Location(1, 1)
    driver1 = Driver('boby', l1, 2)
    driver1.remove_destination()
    assert driver1._destination == None

def test_change_location() -> None:
    """Testing changing the location of the driver."""
    l1 = Location(1, 1)
    l2 = Location(2,2)
    driver1 = Driver('boby', l1, 2)
    driver1.change_location(l2)
    assert driver1.location == l2

if __name__ == '__main__':
    import pytest
    pytest.main(['test_driver.py'])