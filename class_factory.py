from typing import List

from havok_types import havok_types


primative_types = [
    'int',
    'bool',
    'str',
    'float'
]


def add_import(class_imports: dict, class_name: str, source_file=None):
    if source_file is None:
        source_file = class_name

    if source_file not in class_imports:
        class_imports[source_file] = []

    if class_name not in class_imports[source_file]:
        class_imports[source_file].append(class_name)


def class_factory(data: dict, enum_map: dict):
    class_imports = {}
    class_members = []

    parent = '(object)'
    if data['parent'] is not None:
        parent = "({})".format(data['parent'])
        add_import(class_imports, data['parent'])

    if len(data['enums']) > 0:
        add_import(class_imports, 'Enum', 'enum')

    for member in data['members']:
        if member['cl'] is None:
            member_type = havok_types[member['type']].python_type.__name__
            if member['type'] == 'TYPE_ENUM':
                if member['enum'] in enum_map:
                    member_type = enum_map[member['enum']]
                    add_import(class_imports, enum_map[member['enum']], 'enums')
                else:
                    pass
                    # print("Unknown enum: {}".format(member))

            elif member_type not in primative_types:
                add_import(class_imports, member_type, 'common')
        else:
            member_type = member['cl']
            add_import(class_imports, member['cl'])

        class_members.append({
            'name': member['name'],
            'type': member_type
        })

    # print(class_imports)
    # print(class_members)

    with open('havok_classes/{}.py'.format(data['name']), 'w') as outfile:
        for import_source_file in class_imports:
            if import_source_file == 'enum':
                outfile.write("from enum import Enum\n")
            else:
                outfile.write("from .{source_file} import {class_name}\n".format(**{
                    'source_file': import_source_file,
                    'class_name': ', '.join(class_imports[import_source_file])
                }))

        if (len(class_imports) > 0):
            outfile.write("\n\n")

        for enum in data['enums']:
            outfile.write("class {enum_name}(Enum):\n".format(**{
                'enum_name': enum['name']
            }))

            for item in enum['items']:
                outfile.write("    {name} = {value}\n".format(**{
                    'name': item[1],
                    'value': item[0]
                }))

            outfile.write("\n\n")

        outfile.write("class {class_name}{parent}:\n".format(**{
            'class_name': data['name'],
            'parent': parent
        }))

        for member in class_members:
            outfile.write("    {name}: {type}\n".format(**{
                'name': member['name'],
                'type': member['type']
            }))

        if len(class_members) == 0:
            outfile.write("    pass\n")
