from havok_types import havok_types


def class_factory(data: dict):
    file_contents = ''
    imports = []
    members = []

    parent = '(object)'
    if data['parent'] is not None:
        parent = "({})".format(data['parent'])
        imports.append(data['parent'])

    for member in data['members']:
        if member['cl'] is None:
            member_type = havok_types[member['type']].python_type.__name__
        else:
            member_type = member['cl']
            imports.append(member['cl'])

        members.append({
            'name': member['name'],
            'type': member_type
        })

    print(imports)
    print(members)

    with open('havok_classes/{}.py'.format(data['name']), 'w') as outfile:
        for import_class in imports:
            outfile.write("from .{0} import {0}\n".format(import_class))
        outfile.write("\n\n")

        outfile.write("class {class_name}{parent}:\n".format(**{
            'class_name': data['name'],
            'parent': parent
        }))

        for member in members:
            outfile.write("\t{name}: {type}\n".format(**{
                'name': member['name'],
                'type': member['type']
            }))
