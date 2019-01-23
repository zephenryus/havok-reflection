import json

from class_factory import class_factory


def main():
    with open('reflection_data.json', 'r') as infile:
        reflection_data = json.load(infile)

    for havok_class in reflection_data['classes']:
        class_factory(reflection_data['classes'][havok_class])


if __name__ == '__main__':
    main()
