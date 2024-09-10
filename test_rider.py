from rider import Rider
from location import Location

def test_rider_initializer() -> None:
    """Testing the initializer for the rider."""
    l1 = Location(1, 1)
    l2 = Location (2,2)
    rider = Rider('bob', 100, l1, l2)
    assert rider.id == 'bob'
    assert rider.patience == 100
    assert rider.origin == l1
    assert rider.destination == l2
    assert rider.status == "waiting"

def test_cancel_trip() -> None:
    """Testing cancelling trip for the rider."""
    l1 = Location(1, 1)
    l2 = Location (2,2)
    rider = Rider('bob', 100, l1, l2)
    rider.cancel_trip()
    assert rider.status == 'cancelled'

def test_change_status() -> None:
    """Testing changing status for the rider."""
    l1 = Location(1, 1)
    l2 = Location (2,2)
    rider = Rider('bob', 100, l1, l2)
    assert rider.status == "waiting"

    rider.change_status('cancelled')
    assert rider.status == 'cancelled'

    rider.change_status('satisfied')
    assert rider.status == 'satisfied'

if __name__ == '__main__':
    import pytest
    pytest.main(['test_rider.py'])