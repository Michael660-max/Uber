from location import Location, deserialize_location, manhattan_distance

def test_str() -> None:
    """Testing str(Location)."""
    loc1 = Location(1, 2)
    assert str(loc1) == "(1, 2)"
    
    loc2 = Location(0, 0)
    assert str(loc2) == "(0, 0)"

def test_eq() -> None:
    """Testing if 2 of the same locations are equal."""
    loc1 = Location(0, 2)
    loc2 = Location(0, 2)
    loc3 = Location(0, 0)
    assert loc1 == loc2
    assert loc1 != loc3
    
def test_manhattan_distance_same_location() -> None:
    """Test if the manhatten distance for the same location."""
    loc1 = Location(0, 3)
    loc2 = Location(0, 3)
    assert manhattan_distance(loc1, loc2) == 0
    
def test_manhattan_distance_normal() -> None:
    """Test the manhatten distance for normal inputs."""
    loc1 = Location(2, 3)
    loc2 = Location(4, 5)
    assert manhattan_distance(loc1, loc2) == 4
    assert manhattan_distance(loc2, loc1) == 4
    
def test_deserialize_location() -> None:
    """Test deserialize location."""
    assert deserialize_location("(0, 0)") == Location(0, 0)
    assert deserialize_location("(4,2)") == Location(4, 2)

if __name__ == '__main__':
    import pytest
    pytest.main(['test_location.py'])