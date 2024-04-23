from lib.high_value import *

def test_first_value_assigned():
    instance_of_high_value = HighValue(1, 2)
    assert instance_of_high_value.value_first == 1

def test_second_value_assigned():
    instance_of_low_value = HighValue(1, 2)
    assert instance_of_low_value.value_second == 2

def test_see_which_value_is_higher_one():
    instance_values = HighValue(1, 10)
    assert instance_values.get_highest() == "Second value is higher"

def test_see_which_value_is_higher_two():
    instance_values = HighValue(10, 1)
    assert instance_values.get_highest() == "First value is higher"

def test_see_if_values_are_equal():
    instance_values = HighValue(10, 10)
    assert instance_values.get_highest() == "Values are equal"

def test_first_instance_if_value_is_first():
    instance_value = HighValue(5, 8)
    instance_value.add(4, "first")
    assert instance_value.value_first == 9

def test_second_instance_if_value_is_second():
    instance_value = HighValue(8, 10)
    instance_value.add(10, "second")
    assert instance_value.value_second == 20