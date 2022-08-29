import csv

import pytest
from course_18.func.operation import my_add

def get_csv():
    with open("../data/params_csv.csv") as file:
        raw = csv.reader(file)

        data = []
        for line in raw:
            data.append(line)
    print(data)
    return data

class TestWithCsv:
    @pytest.mark.parametrize('x, y, expected', get_csv())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)

