import pytest

from solution import Solution


test_cases = [
    ([[2, 1, 5], [3, 3, 7]], 4, False),
    ([[2, 1, 5], [3, 3, 7]], 5, True),
]


@pytest.mark.parametrize("trips,capacity,expected", test_cases)
def test_carPooling(trips: list[list[int]], capacity: int, expected: bool):
    got = Solution().carPooling(trips, capacity)
    assert got is expected


@pytest.mark.parametrize("trips,capacity,expected", test_cases)
def test_optimized(trips: list[list[int]], capacity: int, expected: bool):
    got = Solution().optimized(trips, capacity)
    assert got is expected
