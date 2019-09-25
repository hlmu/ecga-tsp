"""
Parse data in the data/ directory.
"""


class Parser:
    """
    Given the filename of a tsp file, return a dictionary containing the data given in the file.
    """
    def __init__(self, filename):
        # data consisting of fields such as NAME, TYPE and the map itself
        mp = []
        self.data = {}
        # link map to data
        self.data['map'] = mp
        node_section = False
        with open(filename, 'r') as f:
            for line in f:
                if not node_section:
                    buf = [x.strip() for x in line.split(':')]
                    if len(buf) != 1:
                        self.data[buf[0]] = buf[1]
                    elif buf[0] == 'NODE_COORD_SECTION':
                            node_section = True
                else:
                    if line.strip() == 'EOF':
                        break
                    mp.append([eval(x) for x in line.split()])


        pass

if __name__ == '__main__':
    parser = Parser('data/eil51.tsp')
