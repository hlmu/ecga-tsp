"""
Parse data in the data/ directory.
Given the filename of a tsp file, return a dictionary containing the data given in the file.
"""


def parse(file_name):
    data = {}
    # data consisting of fields such as NAME, TYPE and the map itself
    mp = []
    # link map to data
    data['map'] = mp
    node_section = False
    with open(file_name, 'r') as f:
        for line in f:
            if not node_section:
                buf = [x.strip() for x in line.split(':')]
                if len(buf) != 1:
                    data[buf[0]] = buf[1]
                elif buf[0] == 'NODE_COORD_SECTION':
                        node_section = True
            else:
                if line.strip() == 'EOF':
                    break
                mp.append([eval(x) for x in line.split()])
    return data

