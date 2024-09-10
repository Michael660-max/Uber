"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
WAITING: A constant used for the waiting rider status.
CANCELLED: A constant used for the cancelled rider status.
SATISFIED: A constant used for the satisfied rider status
"""

from location import Location

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:
    """A rider for a ride-sharing service.

    === Public Attributes ===
    id: A unique identifier for the rider.
    origin: The original location of the rider.
    destination: The rider's destination
    status: The current status of the rider.
    patience: The time indicating how long the rider is willing to wait.
    """
    id: str
    patience: int
    origin: Location
    destination: Location
    status: str

    def __init__(self, identifier: str, patience: int, origin: Location,
                 destination: Location) -> None:
        """Initialize a Rider.

        """
        self.id = identifier
        self.patience = patience
        self.origin = origin
        self.destination = destination
        self.status = WAITING

    def cancel_trip(self) -> None:
        """Cancel trip.

        """
        self.status = CANCELLED

    def change_status(self, status: str) -> None:
        """Change the rider's status.

        """
        if status in [WAITING, CANCELLED, SATISFIED]:
            self.status = status


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['location']})
