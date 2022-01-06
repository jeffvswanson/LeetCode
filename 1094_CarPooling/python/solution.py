"""
1094. Car Pooling

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot
turn around and drive west).

You are given the integer capacity and an array trips where
trip[i] = [numPassengers_i, from_i, to_i] indicates that the ith trip has
numPassengers_i passengers and the locations to pick them up and drop them off are
from_i and to_i respectively. The locations are given as the number of kilometers due
east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given
trips, or false otherwise.

Examples 
--------
Example 1:
    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false

Example 2:
    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true

Constraints
-----------
* 1 <= trips.length <= 1000
* trips[i].length == 3
* 1 <= numPassengers_i <= 100
* 0 <= from_i < to_i <= 1000
* 1 <= capacity <= 105
"""


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # We can create a dictionary that holds the different miles as keys and the
        # number of passengers as values
        # As we iterate through the list add the values to the key in the dictionary
        # If when adding the value it exceeds the capacity we are done
        # Otherwise if we get to the end of the trips list we are capable of
        # transporting all of the passengers
        seats_to_passengers = {}
        for trip in trips:
            num_passengers, start, stop = trip
            for mile in range(start, stop):
                if mile not in seats_to_passengers:
                    seats_to_passengers[mile] = 0
                seats_to_passengers[mile] += num_passengers
                if seats_to_passengers[mile] > capacity:
                    return False
        return True

    def optimized(self, trips: list[list[int]], capacity: int) -> bool:
        max_mileage = 1001  # given by constraints
        # positive more passengers get in
        # negative more passengers get out
        net_passengers_at_mile_marker = [0] * max_mileage

        for num_passengers, start, end in trips:
            # passengers getting in
            net_passengers_at_mile_marker[start] += num_passengers
            # passengers getting out
            net_passengers_at_mile_marker[end] -= num_passengers

        passengers_in_car = 0
        for net_passenger_movement in net_passengers_at_mile_marker:
            passengers_in_car += net_passenger_movement
            if passengers_in_car > capacity:
                return False
        return True
