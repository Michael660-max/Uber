from simulation import Simulation
from event import RiderRequest, DriverRequest
from rider import Rider
from driver import Driver
from location import Location

def test_run_min() -> None:
    """Testing simulation on min number of inital events."""
    l1 = Location(1, 1)
    d1 = Location(2, 2)
    rider = Rider('bob', 10, l1, d1)
    e1 = RiderRequest(10, rider)

    l1 = Location(1, 1)
    driver = Driver('bobby', l1, 1)
    e2 = DriverRequest(10, driver)
    
    initial_events = [e1, e2]
    sim = Simulation()
    data = sim.run(initial_events)
    assert type(data) == dict

if __name__ == '__main__':
    import pytest
    pytest.main(['test_simulation.py'])