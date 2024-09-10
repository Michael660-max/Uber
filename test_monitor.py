from monitor import Monitor, Activity
from location import Location

def test_average_wait_time_min():
    """Calculate average wait time with min number of events."""
    # Environemntal Setup
    monitor = Monitor()
    l2 = Location(1,5)
    l3 = Location(2,2)
    monitor.notify(15, 'rider', 'request', 'bobby', l2)    
    monitor.notify(15, 'rider', 'cancel', 'bobby', l3)    

    #Testing same time event
    assert monitor._average_wait_time() == 0
    monitor._activities['rider']['bobby'].pop()

    #Testing different time event
    monitor.notify(20, 'rider', 'cancel', 'bobby', l3)    
    assert monitor._average_wait_time() == 5

def test_average_total_distance_min():
    """Calculate average total distance with min number of drivers."""
    monitor = Monitor()
    l1 = Location(1,1)
    monitor.notify(100, 'driver', 'request', 'bob', l1)    
    assert monitor._average_ride_distance() == 0

def test_average_total_distance_two():
    """Calculate average total distance with 2 events."""
    monitor = Monitor()
    l1 = Location(1,1)
    l2 = Location(2,2)
    monitor.notify(100, 'driver', 'request', 'bob', l1)
    monitor.notify(110, 'driver', 'pickup', 'bob', l2)
        
    assert monitor._average_total_distance() == 2

def test_average_total_distance_many():
    """Calculate average total distance with many events."""
    monitor = Monitor()
    l1 = Location(1,1)
    l2 = Location(2,2)
    l3 = Location(0,0)
    l4 = Location(5,5)
    l5 = Location(10,10)
    monitor.notify(100, 'driver', 'request', 'bob', l1)
    monitor.notify(110, 'driver', 'pickup', 'bob', l2)
    monitor.notify(110, 'driver', 'dropoff', 'bob', l3)
    monitor.notify(110, 'driver', 'request', 'bob', l4)
    monitor.notify(110, 'driver', 'pickup', 'bob', l5)

    monitor.notify(110, 'driver', 'pickup', 'bobby', l5)
    monitor.notify(110, 'driver', 'pickup', 'bobbline', l5)

    assert monitor._average_total_distance() == 26 / 3

def test_average_ride_distance_min():
    """Calculate average ride distance with min events."""
    monitor = Monitor()
    l1 = Location(1,1)
    monitor.notify(100, 'driver', 'pickup', 'bob', l1)
    
    assert monitor._average_total_distance() == 0
    monitor._activities['driver']['bob'].pop()

    monitor.notify(100, 'driver', 'dropoff', 'bob', l1)
    assert monitor._average_total_distance() == 0

def test_average_ride_distance_two_non_ride():
    """Calculate average ride distance with 2 non ride events."""
    monitor = Monitor()
    l1 = Location(1,1)
    l2 = Location(2,2)
    monitor.notify(100, 'driver', 'request', 'bob', l1)
    monitor.notify(100, 'driver', 'pickup', 'bob', l2)
    assert monitor._average_ride_distance() == 0

    monitor._activities['driver']['bob'].pop()
    monitor._activities['driver']['bob'].pop()
    monitor.notify(100, 'driver', 'dropoff', 'bob', l1)
    monitor.notify(100, 'driver', 'request', 'bob', l2)
    assert monitor._average_ride_distance() == 0

def test_average_ride_distance_many():
    """Calculate average ride distance with many ride events."""
    monitor = Monitor()
    l1 = Location(1,1)
    l2 = Location(2,2)
    l3 = Location(0,0)
    l4 = Location(5,5)
    l5 = Location(10,10)

    monitor.notify(100, 'driver', 'request', 'bob', l1)
    monitor.notify(110, 'driver', 'pickup', 'bob', l2)
    monitor.notify(110, 'driver', 'dropoff', 'bob', l3)
    monitor.notify(110, 'driver', 'request', 'bob', l4)
    monitor.notify(110, 'driver', 'pickup', 'bob', l5)

    monitor.notify(110, 'driver', 'pickup', 'bobby', l5)
    monitor.notify(110, 'driver', 'dropoff', 'bobbline', l5)
    
    monitor.notify(110, 'driver', 'request', 'bobette', l4)
    monitor.notify(110, 'driver', 'pickup', 'bobette', l4)
    monitor.notify(110, 'driver', 'dropoff', 'bobette', l5)

    assert monitor._average_ride_distance() == 14 / 4


if __name__ == '__main__':
    import pytest
    pytest.main(['test_monitor.py'])