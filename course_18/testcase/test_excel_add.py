import openpyxl
import pytest
from course_18.func.operation import my_add


def test_get_excle():
    book = openpyxl.load_workbook('../data/datapa.xlsx')
    sheet = book.active
    cells = sheet["A1":"C3"]
    print(cells)
    values = []
    for row in cells:
        data = []
        for cell in row:
            data.append(cell.value)
        values.append(data)
    print(values)
    return values

class TestWithExcel:
    @pytest.mark.parametrize('x, y, expected', test_get_excle())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)