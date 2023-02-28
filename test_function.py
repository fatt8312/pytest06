from function import number_to_month, validate_number
import pytest


@pytest.mark.code    #pytest -m code
def test_january_input_1():
    input = 1
    expected_result = "january"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code    #pytest -m code
def test_february_input_2():
    input = 2
    expected_result = "february"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code    #pytest -m code
def test_march_input_3():
    input = 3
    expected_result = "march"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code    #pytest -m code
def test_april_input_4():
    input = 4
    expected_result = "april"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code    #pytest -m code
def test_May_input_5():
    input = 5
    expected_result = "May"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code    #pytest -m code
def test_June_input_6():
    input = 6
    expected_result = "June"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code    #pytest -m code
def test_July_input_7():
    input = 7
    expected_result = "July"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code    #pytest -m code
def test_August_input_8():
    input = 8
    expected_result = "August"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code    #pytest -m code
def test_September_input_9():
    input = 9
    expected_result = "September"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code    #pytest -m code
def test_October_input_10():
    input = 10
    expected_result = "October"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code    #pytest -m code
def test_November_input_11():
    input = 11
    expected_result = "November"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code    #pytest -m code
def test_December_input_12():
    input = 12
    expected_result = "December"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_out_of_range_input_0():
    input = 0
    expected_result = "out_of_range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_out_of_range_input_13():
    input = 13
    expected_result = "out_of_range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_out_of_range_input_10():
    input = -10
    expected_result = "out_of_range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_out_of_range_input_22():
    input = -22
    expected_result = "out_of_range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_input_integer_input_1_1():
    input = 1.1
    expected_result = "input_integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_out_of_range_input_13_1():
    input = 13.1
    expected_result = "out_of_range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_input_integer_input_char_a():
    input = "a"
    expected_result = "input_integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_input_integer_input_char_sharp():
    input = "#"
    expected_result = "input_integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_1_input_1():
    input = 1
    expected_result = 1
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_12_input_12():
    input = 12
    expected_result = 12
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_out_of_range_input_0_5():
    input = 0.5
    expected_result = "out_of_range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_out_of_range_input_1_5():
    input = -1.5
    expected_result = "out_of_range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_input_integer_input_1_1():
    input = 1.1
    expected_result = "input_integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate    #pytest -m validate
def test_input_integer_input_1_5():
    input = 1.5
    expected_result = "input_integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result