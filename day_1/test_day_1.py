import pytest

from day_1 import get_values_for_calibration

@pytest.mark.parametrize("data,expected", [("1abc2", 12),("pqr3stu8vwx", 38),("a1b2c3d4e5f", 15),("treb7uchet", 77)])
def test_calibration_values(data,expected):
    # GIVEN
    # WHEN
    result = get_values_for_calibration(data)
    # THEN
    assert expected == result