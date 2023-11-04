import Lab2

def test_min_max():
    input_arr = [2, 32, 6, 75]
    result = Lab2.calc_min_max_temperature(input_arr)
    assert (result == (2, 75))

def test_calc_average():
    input_arr = [4, 8, 16, 32]
    result = Lab2.calc_average_temperature(input_arr)
    assert (result == (15))

def test_median_temperature():
    input_arr = [2, 4, 1, 6, 9]
    result = Lab2.calc_median_temperature(input_arr)
    assert (result == 4)