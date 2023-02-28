from function import display_month
import pytest

@pytest.mark.display        #pytest -m display
@pytest.mark.parametrize('input_number,expected_result', [
    (1,"january"),(2,"february"),(3,"march"),(4,"april"),
    (5,"May"),(6,"June"),(7,"July"),(8,"August"),(9,"September"),
    (10,"October"),(11,"November"),(12,"December")
    ,(0,"out_of_range"),
    (13,"out_of_range"),(-10,"out_of_range"),(22,"out_of_range"),
    (1.1,"input_integer"),(13.1,"out_of_range"),("a","input_integer"),
    ("#","input_integer"),(0.5,"out_of_range"),(-1.5,"out_of_range"),
    (1.5,"input_integer")
    ])

def test_display(input_number,expected_result):
     actual_result = display_month(input_number)
     assert expected_result == actual_result