import json


def get_json():
    with open('../data/params.json') as file:
        data = json.loads(file.read())
        print(data, type(data))

        s = json.dumps(data, ensure_ascii=False)
        print(s, type(s))

if __name__ == '__main__':
    get_json()