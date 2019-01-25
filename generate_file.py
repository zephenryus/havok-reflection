from havok_types import havok_types


def write_file(data, class_data):
    parent = class_data['parent']
    class_imports = class_data['class_imports']
    class_members = class_data['class_members']

    with open('havok_classes/{}.py'.format(data['name']), 'w') as outfile:
        print('Generating havok_classes/{}.py...'.format(data['name']))
        _write_imports(outfile, class_imports)

        if len(class_imports) > 0:
            outfile.write("\n\n")

        _write_enums(outfile, data)
        _write_class_header(outfile, data, parent)
        _write_class_members(outfile, class_members)
        _write_constructor(outfile, class_members)
        _write_representations(outfile, class_members)


def _write_imports(outfile, class_imports):
    for import_source_file in class_imports:
        if import_source_file == 'enum':
            outfile.write("from enum import Enum\n")

        elif import_source_file == 'struct':
            outfile.write("import struct\n")

        elif import_source_file == 'typing':
            outfile.write("from typing import {class_name}\n".format(**{
                'class_name': ', '.join(class_imports[import_source_file])
            }))

        else:
            outfile.write("from .{source_file} import {class_name}\n".format(**{
                'source_file': import_source_file,
                'class_name': ', '.join(class_imports[import_source_file])
            }))


def _write_enums(outfile, data):
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


def _write_class_header(outfile, data, parent):
    outfile.write("class {class_name}{parent}:\n".format(**{
        'class_name': data['name'],
        'parent': parent
    }))


def _write_class_members(outfile, class_members):
    for member in class_members:
        if member['type'] == 'List':
            outfile.write("    {name}: List[{subtype}]\n".format(**{
                'name': member['name'],
                'subtype': member['subtype']
            }))
        else:
            outfile.write("    {name}: {type}\n".format(**{
                'name': member['name'],
                'type': member['type']
            }))


def _write_constructor(outfile, class_members):
    if len(class_members) == 0:
        outfile.write("    pass\n")

    else:
        outfile.write("\n    def __init__(self, infile):\n")

        for member in class_members:
            if member['unpack_string'] != '':
                outfile.write(
                    "        self.{name} = struct.unpack('>{unpack_string}', infile.read({unpack_size}))  # {reflection_type}:{reflection_subtype}\n".format(
                        **{
                            'name': member['name'],
                            'unpack_string': member['unpack_string'],
                            'unpack_size': member['unpack_size'],
                            'reflection_type': member['reflection_type'],
                            'reflection_subtype': member['reflection_subtype']
                        }))
            else:
                if member['type'] == 'List':
                    outfile.write(
                        "        self.{name} = get_array(infile, {subtype}, {unpack_size})  # {reflection_type}:{reflection_subtype}\n".format(
                            **{
                                'name': member['name'],
                                'subtype': member['subtype'],
                                'unpack_size': havok_types[member['reflection_subtype']].struct_size,
                                'reflection_type': member['reflection_type'],
                                'reflection_subtype': member['reflection_subtype']
                            }))

                elif member['reflection_type'] == 'TYPE_ARRAY':
                    outfile.write(
                        "        self.{name} = get_array(infile, {type})  # {reflection_type}:{reflection_subtype}\n".format(
                            **{
                                'name': member['name'],
                                'type': member['type'],
                                'reflection_type': member['reflection_type'],
                                'reflection_subtype': member['reflection_subtype']
                            }))

                else:
                    outfile.write(
                        "        self.{name} = {type}(infile)  # {reflection_type}:{reflection_subtype}\n".format(**{
                            'name': member['name'],
                            'type': member['type'],
                            'reflection_type': member['reflection_type'],
                            'reflection_subtype': member['reflection_subtype']
                        }))


def _write_representations(outfile, class_members):
    outfile.write('\n    def __repr__(self):\n        return "<{class_name} ')

    outfile.write(', '.join(map(
        lambda x: _get_member_repr_function(x),
        class_members
    )))

    outfile.write('>".format(**{\n            "class_name": self.__class__.__name__,\n')

    for class_member in class_members:
        outfile.write('            "{0}": self.{0},\n'.format(
            class_member['name']
        ))

    outfile.write("        })\n")


def _get_member_repr_function(member):
    repr_string = '{}='.format(member['name'])

    left_delimiter = ''
    right_delimiter = ''

    if member['type'] == 'List':
        left_delimiter = '['
        right_delimiter = ']'

    elif member['type'] == 'str':
        left_delimiter = "\\\""
        right_delimiter = "\\\""

    repr_string += '{}{}{}{}{}'.format(
        left_delimiter,
        '{',
        member['name'],
        '}',
        right_delimiter
    )

    return repr_string
