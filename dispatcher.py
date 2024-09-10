"""Dispatcher for the simulation"""

from typing import Optional
from driver import Driver
from rider import Rider


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """
    # === Private Attributes ===
    # _available_drivers: A list of drivers that are available
    # _waiting_riders: A list of available riders

    _available_drivers: dict[id, Driver]
    _waiting_riders: list[Rider]

    def __init__(self) -> None:
        """Initialize a Dispatcher.

        """
        self._available_drivers = {}
        self._waiting_riders = []

    def __str__(self) -> str:
        """Return a string representation.

        """
        return f'({str(self._available_drivers)}, {str(self._waiting_riders)})'

    def request_driver(self, rider: Rider) -> Optional[Driver]:
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        """
        if len(self._available_drivers) == 0:
            self._waiting_riders.append(rider)
            return None
        else:
            time_needed = {}
            for driver in self._available_drivers.values():
                if driver.is_idle:
                    time_needed[driver.get_travel_time(rider.origin)] = driver
            fastest_time = min(time_needed.keys())

            if rider in self._waiting_riders:
                self._waiting_riders.remove(rider)
            return time_needed[fastest_time]

    def request_rider(self, driver: Driver) -> Optional[Rider]:
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        """
        if driver.id not in self._available_drivers:
            self._available_drivers[driver.id] = driver

        if self._waiting_riders == []:
            return None
        else:
            return self._waiting_riders.pop(0)

    def cancel_ride(self, rider: Rider) -> None:
        """Cancel the ride for rider.

        """
        rider.cancel_trip()
        if rider in self._waiting_riders:
            self._waiting_riders.remove(rider)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['typing', 'driver', 'rider']})
