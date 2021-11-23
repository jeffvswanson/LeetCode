import pytest

import solution


@pytest.mark.parametrize("num_versions,bad_version", [(10, 1), (10, 8), (1, 1), (10, 10), (10, 5)])
def test_initial_pass(num_versions, bad_version):
    got = solution.initial_pass(num_versions, bad_version)
    assert got == bad_version
