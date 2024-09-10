from event import create_event_list, RiderRequest, DriverRequest, Pickup, Dropoff, Cancellation
from location import Location
from monitor import Monitor
from dispatcher import Dispatcher
from driver import Driver
from rider import Rider

def test_create_event_list() -> None:
    """Test create_event_list on a normal set of inputs."""
    events = create_event_list("events.txt")
    assert len(events) == 12

    d1 = events[2]
    assert d1.timestamp == 0
    assert d1.driver.id == 'Crocus'
    assert d1.driver.location == Location(3, 1)
    assert d1.driver.speed == 1

    r1 = events[8]
    assert r1.timestamp == 10
    assert r1.rider.id == 'Cerise'
    assert r1.rider.origin == Location(4, 2)
    assert r1.rider.destination == Location(1, 5)
    assert r1.rider.patience == 15

    # Rider:
    #   1) Request -> Cancellation -> []
    #   2) Request -> Pickup -> Cancellation -> Dropoff
    #   3) Request -> Cancellation -> Pickup
    # Driver:
    #   1) Request
    #   2) Request -> Pickup (Cancellation) -> {Repeat}
    #   3) Request -> Pickup -> Dropoff -> {Repeat}


def test_driver_request_none() -> None:
    """Test DriverRequest without available rider."""
    events = create_event_list("events.txt")
    driver_request = events[2]
    monitor = Monitor()
    dispatcher = Dispatcher()
    driver_events = driver_request.do(dispatcher, monitor)

    assert len(driver_events) == 0
    assert len(monitor._activities["driver"]["Crocus"]) == 1
    assert monitor._activities["driver"]["Crocus"][0].time == 0 

def test_rider_request_none() -> None:
    """Test RiderRequest without available driver."""
    events = create_event_list("events.txt")
    rider_request = events[8]
    monitor = Monitor()
    dispatcher = Dispatcher()
    rider_events = rider_request.do(dispatcher, monitor)

    assert len(monitor._activities["rider"]["Cerise"]) == 1
    assert len(rider_events) == 1
    assert type(rider_events[0]) == Cancellation

def test_driver_request() -> None:
    """Test DriverRequest with available driver."""
    events = create_event_list("events.txt")
    driver_request, rider_request = events[2], events[8]
    driver, rider = driver_request.driver, rider_request.rider
    monitor = Monitor()
    dispatcher = Dispatcher()
    rider_request.do(dispatcher, monitor)
    driver_events = driver_request.do(dispatcher, monitor)
    
    assert len(monitor._activities["driver"]["Crocus"]) == 1
    assert len(driver_events) == 1
    assert driver.location == rider.origin

def test_rider_request() -> None:
    """Test RiderRequest with available rider."""
    events = create_event_list("events.txt")
    driver_request, rider_request = events[2], events[8]
    driver, rider = driver_request.driver, rider_request.rider
    monitor = Monitor()
    dispatcher = Dispatcher()
    driver_request.do(dispatcher, monitor)
    rider_events = rider_request.do(dispatcher, monitor)
    
    assert len(monitor._activities["rider"]["Cerise"]) == 1
    assert len(rider_events) == 2
    assert type(rider_events[0]) == Pickup
    assert type(rider_events[1]) == Cancellation
    assert driver.location == rider.origin

def test_cancellation_request() -> None:
    """Test CancellationRequest."""
    events = create_event_list("events.txt")
    rider_request = events[8]
    rider = rider_request.rider
    monitor = Monitor()
    dispatcher = Dispatcher()
    rider_events = rider_request.do(dispatcher, monitor)

    result = rider_events[0].do(dispatcher, monitor)
    assert len(result) == 0
    assert rider.status == 'cancelled'
    assert len(monitor._activities["rider"]["Cerise"]) == 2
    assert monitor._activities["rider"]["Cerise"][0].description == "request"

    assert monitor._activities["rider"]["Cerise"][0].time == 10
    assert monitor._activities["rider"]["Cerise"][1].time == 25

    
def test_pickup_request() -> None:
    """Test PickupRequest."""
    #Environmental Setup (ES)
    events = create_event_list("test_events1.txt")
    driver_request, rider_request = events[0], events[1]
    rider = rider_request.rider
    monitor = Monitor()
    dispatcher = Dispatcher()
    rider_result = rider_request.do(dispatcher, monitor)
    driver_result = driver_request.do(dispatcher, monitor)
    
    #Request
    # Rider: Request -> Pickup -> Cancellation(redundant)
    # Driver: Request -> Pickup -> Dropoff
    assert monitor._activities["rider"]["Cerise"][0].time == 0
    assert monitor._activities["driver"]["Crocus"][0].time == 10
    assert type(rider_result[0]) == Cancellation
    assert type(driver_result[0]) == Pickup

    #Pickup
    assert driver_result[0].timestamp < rider_result[0].timestamp
    result = driver_result[0].do(dispatcher, monitor)
    assert len(monitor._activities["rider"]["Cerise"]) == 2
    assert len(monitor._activities["driver"]["Crocus"]) == 2
    assert monitor._activities["rider"]["Cerise"][1].description == "pickup"
    assert monitor._activities["driver"]["Crocus"][1].description == "pickup"
    assert monitor._activities["rider"]["Cerise"][1].time == 16
    assert monitor._activities["driver"]["Crocus"][1].time == 16

    assert len(result) == 1
    assert type(result[0]) == Dropoff
    assert rider.status == 'satisfied'
    

def test_pickup_request_cancelled() -> None:
    """Test PickupRequest when rider cancels."""
    events = create_event_list("events.txt")
    driver_request, rider_request = events[2], events[8]
    rider, driver = rider_request.rider, driver_request.driver
    monitor = Monitor()
    dispatcher = Dispatcher()
    driver_request.do(dispatcher, monitor)
    rider_result = rider_request.do(dispatcher, monitor)
    rider.cancel_trip()

    assert type(rider_result[0]) == Pickup
    result = rider_result[0].do(dispatcher, monitor)
    assert len(result) == 1
    assert type(result[0]) == DriverRequest
    assert driver._destination == None

def test_dropoff() -> None:
    """Test Dropoff."""
    #ES
    #Environmental Setup (ES)
    events = create_event_list("test_events1.txt")
    driver_request, rider_request = events[0], events[1]
    rider, driver = rider_request.rider, driver_request.driver
    monitor = Monitor()
    dispatcher = Dispatcher()
    rider_request.do(dispatcher, monitor)
    driver_result = driver_request.do(dispatcher, monitor)
    result = driver_result[0].do(dispatcher, monitor)
    
    #Dropoff
    final_result = result[0].do(dispatcher, monitor)
    assert len(monitor._activities["driver"]["Crocus"]) == 3
    assert monitor._activities["driver"]["Crocus"][2].time == 20
    assert driver.location == rider.destination
    assert driver._destination == None
    assert len(final_result) == 1
    assert type(final_result[0]) == DriverRequest


if __name__ == '__main__':
    import pytest
    pytest.main(['test_event.py'])