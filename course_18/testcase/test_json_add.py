import json
import pytest
from course_18.func.operation import my_add


def get_json():
    with open("../data/params_json2.json", 'r') as file:
        data = json.loads(file.read())
    return list(data.values())


class TestWithjson:
    @pytest.mark.parametrize('x, y, expected', get_json())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)