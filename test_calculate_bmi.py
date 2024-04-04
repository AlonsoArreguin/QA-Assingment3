from main import calculate_bmi


def test_underweight():
    bmi, category = calculate_bmi(60, 80)
    assert category == "Underweight"

def test_normal_weight():
    bmi, category = calculate_bmi(65, 140)
    assert category == "Normal weight"

def test_overweight():
    bmi, category = calculate_bmi(70, 180)
    assert category == "Overweight"

def test_obese():
    bmi, category = calculate_bmi(72, 220)
    assert category == "Obese"



# Additional boundary test cases

def test_underweight_boundary_below():
    # Just below the underweight category
    bmi, category = calculate_bmi(59.5, 78)
    assert category == "Underweight"

def test_underweight_boundary_above():
    # Just above the underweight category
    bmi, category = calculate_bmi(58, 86.5)
    assert category == "Normal weight"

def test_normal_weight_boundary_below():
    # Just below the normal weight category
    bmi, category = calculate_bmi(64, 105)
    assert category == "Normal weight"

def test_normal_weight_boundary_above():
    # Just above the normal weight category
    bmi, category = calculate_bmi(63, 142)
    assert category == "Overweight"

def test_overweight_boundary_below():
    # Just below the overweight category
    bmi, category = calculate_bmi(69.9, 179)
    assert category == "Overweight"

def test_overweight_boundary_above():
    # Just above the overweight category
    bmi, category = calculate_bmi(67, 188)
    assert category == "Obese"

def test_obese_boundary_below():
    # Just below the obese category
    bmi, category = calculate_bmi(71.9, 219)
    assert category == "Obese"