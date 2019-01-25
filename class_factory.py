from havok_types import havok_types

primative_types = [
    'int',
    'bool',
    'str',
    'float'
]


def class_factory(data: dict, enum_map: dict):
    class_imports = {}

    parent = _get_parent_string(data, class_imports)
    _add_enum_import(data, class_imports)
    class_members = _get_class_members(data, class_imports, enum_map)

    return {
        'parent': parent,
        'class_imports': class_imports,
        'class_members': class_members
    }


def add_import(class_imports: dict, class_name: str, source_file=None):
    if source_file is None:
        source_file = class_name

    if source_file not in class_imports:
        class_imports[source_file] = []

    if class_name not in class_imports[source_file]:
        class_imports[source_file].append(class_name)


def _get_parent_string(data, class_imports):
    parent = '(object)'
    if data['parent'] is not None:
        parent = "({})".format(data['parent'])
        add_import(class_imports, data['parent'])

    return parent


def _add_enum_import(data, class_imports):
    if len(data['enums']) > 0:
        add_import(class_imports, 'Enum', 'enum')


def _get_class_members(data, class_imports, enum_map):
    class_members = []

    for member in data['members']:
        # if member['cl'] is None:
        #     member_type = _get_member_type(class_imports, enum_map, member, 'type')
        # else:
        #     member_type = member['cl']
        #     add_import(class_imports, member['cl'])

        member_type = _get_member_type(class_imports, enum_map, member, 'type')
        member_subtype = _get_member_type(class_imports, enum_map, member, 'subtype')

        if member['type'] == 'TYPE_STRUCT':
            member_type = member['cl']
            add_import(class_imports, member['cl'])

        if member['cl'] is not None:
            member_subtype = member['cl']
            add_import(class_imports, member['cl'])

        class_members.append({
            'name': member['name'],
            'type': member_type,
            'subtype': member_subtype,
            'unpack_string': havok_types[member['type']].struct_char,
            'unpack_size': havok_types[member['type']].struct_size,
            'reflection_type': member['type'],
            'reflection_subtype': member['subtype'],
        })

        if havok_types[member['type']].struct_size > 0:
            add_import(class_imports, 'struct')

    return class_members


def _get_member_type(class_imports, enum_map, member, key):
    member_type = havok_types[member[key]].python_type.__name__
    if member[key] == 'TYPE_ENUM':
        if member['enum'] in enum_map:
            member_type = enum_map[member['enum']]
            add_import(class_imports, enum_map[member['enum']], 'enums')
        else:
            pass
            # print("Unknown enum: {}".format(member))

    elif member[key] == 'TYPE_ARRAY':
        add_import(class_imports, 'List', 'typing')
        add_import(class_imports, 'get_array', 'common')

    elif member[key] not in primative_types:
        pass
        # add_import(class_imports, member_type, 'common')

    return member_type
