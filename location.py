"""Locations for the simulation"""

from __future__ import annotations


class Location:
    """two-dimensional location.

    === Public Attributes ===
    row:
        Represents the number of blocks from the
        bottom edge of the grid.
    column:
        Represents the number of blocks from the
        left of the grid.

    === Representation Invariant ===
    - row is a non-negative integer
    - column is a non-negative integer
    """
    row: int
    column: int

    def __init__(self, row: int, column: int) -> None:
        """Initialize a location.

        The row and column are greater than or equal to 0.

        """
        self.row = row
        self.column = column

    def __str__(self) -> str:
        """Return a string representation.

        """
        return f'({str(self.row)}, {str(self.column)})'

    def __eq__(self, other: Location) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        if (self.row == other.row) and (self.column == other.column):
            return True
        else:
            return False


def manhattan_distance(origin: Location, destination: Location) -> int:
    """Return the Manhattan distance between the origin and the destination.

    """
    ver = abs(destination.row - origin.row)
    hor = abs(destination.column - origin.column)
    return ver + hor


def deserialize_location(location_str: str) -> Location:
    """Deserialize a location.

    location_str: A location in the format 'row,col'
    """
    loc = []
    for char in location_str:
        if char.isdigit():
            loc.append(int(char))

    return Location(loc[0], loc[1])


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()
    