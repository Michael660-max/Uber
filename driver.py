"""Drivers for the simulation"""

from location import Location, manhattan_distance
from rider import Rider


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    id: A unique identifier for the driver.
    location: The current location of the driver.
    is_idle: True if the driver is idle and False otherwise.
    speed: The speed of the driver
    destinaton: The destination of the driver.
    """

    id: str
    location: Location
    is_idle: bool
    speed: int
    _destination: Location

    def __init__(self, identifier: str, location: Location, speed: int) -> None:
        """Initialize a driver.

        """
        self.id = identifier
        self.location = location
        self.is_idle = True
        self.speed = speed
        self._destination = None

    def __str__(self) -> str:
        """Return a string representation.

        """
        return f'({str(self.id)}, {str(self.location)}, {str(self.speed)})'

    def __eq__(self, other: object) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        if self.id == other.id:
            return True
        else:
            return False

    def get_travel_time(self, destination: Location) -> int:
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        """
        calc = manhattan_distance(self.location, destination) / self.speed
        return round(calc)

    def start_drive(self, location: Location) -> int:
        """Start driving to the location.
        Return the time that the drive will take.

        """
        self.is_idle = False
        travel_time = self.get_travel_time(location)
        self.location = location
        return travel_time

    def end_drive(self) -> None:
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        """
        self.is_idle = True

    def start_ride(self, rider: Rider) -> int:
        """Start a ride and return the time the ride will take.

        """
        self.is_idle = False
        self._destination = rider.destination
        rider.change_status('satisfied')
        return self.get_travel_time(self._destination)

    def end_ride(self) -> None:
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        """
        self.is_idle = True
        self.location = self._destination

    def remove_destination(self) -> None:
        """Remove the destination of the driver.

        """
        self._destination = None
        self.is_idle = True

    def change_location(self, location: Location) -> None:
        """Change the location of the driver.

        """
        self.location = location


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(
        config={'extra-imports': ['location', 'rider']})
