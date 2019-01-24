import json

from class_factory import class_factory
from enum_factory import enum_factory


def main():
    with open('reflection_data.json', 'r') as infile:
        reflection_data = json.load(infile)

    enum_map = {}
    with open('havok_classes/enums.py', 'w') as outfile:
        outfile.write('from enum import Enum\n')
        for havok_enum in reflection_data['enums_by_id']:
            enum_map[int(havok_enum)] = reflection_data['enums_by_id'][havok_enum]['name']
            enum_factory(reflection_data['enums_by_id'], havok_enum, outfile)

    for havok_class in reflection_data['classes']:
        class_factory(reflection_data['classes'][havok_class], enum_map)


if __name__ == '__main__':
    main()
