from typing import TextIO


def enum_factory(data: dict, enum_id: int, outfile: TextIO):
    name = data[enum_id]['name']
    items = data[enum_id]['items']

    outfile.write("\n\nclass {0}(Enum):\n".format(name))
    outfile.write("    # enum id: {}\n\n".format(enum_id))

    for item in items:
        outfile.write("    {} = {}\n".format(
            item[1],
            item[0]
        ))
